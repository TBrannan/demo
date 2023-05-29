from unittest import TestCase
import psycopg2


class TryTesting(TestCase):
    def query_postgres(self, sql):
        try:
            conn = psycopg2.connect(f"dbname=postgres user=travis host=localhost")
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.commit()
            cur.close()

    def get_sql(self, name):
        with open(f"/home/circleci/project/src/sql/{name}.sql") as sql:
            result = self.query_postgres(sql.read())
            return result

    def test_show_tables(self):
        result = self.query_postgres(
            "select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';"
        )
        self.assertEqual(result[0][0], "league")

    def test_run_queries(self):
        self.get_sql("create_table")
        self.get_sql("insert_table")
        query_table = self.get_sql("query_table")
        self.assertEqual(query_table, [(1, "555", "league of legends")])
