from aws_cdk import aws_glue as glue, Stack, aws_s3 as s3, aws_s3_deployment as s3deploy
from constructs import Construct


class GlueStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        glue_bucket = s3.Bucket(
            self, "glue-code-bucket", bucket_name="tbrannan-glue-code"
        )

        bucket_deploy = s3deploy.BucketDeployment(
            self,
            "DeployGlueJobs",
            sources=[s3deploy.Source.asset(".\glue_stack\glue_jobs")],
            destination_bucket=glue_bucket,
        )

        glue_job = glue.CfnJob(
            self,
            "DemoGlueJob",
            name="DemoGlueJob",
            command=glue.CfnJob.JobCommandProperty(
                name="pythonshell",
                python_version="3.9",
                script_location="s3://tbrannan-glue-code/demo_glue_job.py",
            ),
            role="role",
        )

        cfn_trigger = glue.CfnTrigger(
            self,
            "MyCfnTrigger",
            actions=[glue.CfnTrigger.ActionProperty(job_name=glue_job.name)],
            type="SCHEDULED",
            schedule="cron(15 12 * * ? *)",
            start_on_creation=False,
        )
