import psycopg2
from env import dbname, user, host, password


def query_postgres():
    sql = get_sql()
    try:
        conn = psycopg2.connect(
            f"dbname={dbname} user={user} host={host} password={password}"
        )
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        print(result)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_sql():
    with open("src\sql\query.sql") as sql:
        return sql.read()


query_postgres()
