import aws_cdk as core
import aws_cdk.assertions as assertions

from glue_stack.glue_stack_stack import GlueStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in glue_stack/glue_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GlueStackStack(app, "glue-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
