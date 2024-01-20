""" This file is used to test the connection to the database. """
import psycopg2
import os


class Test_db:
    __test__ = False

    def __init__(self) -> None:
        self.dname = os.environ["POSTGRES_DB"]
        self.user = os.environ["POSTGRES_USER"]
        self.password = os.environ["POSTGRES_PASSWORD"]
        self.host = os.environ["POSTGRES_HOST"]
        self.port = os.environ["POSTGRES_PORT"]

    def test_connection(self) -> None:
        try:
            conn = psycopg2.connect(
                database=self.dname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            conn.close()
            return "Connection successful"
        except Exception as e:
            return f"Connection failed\n{e}"
