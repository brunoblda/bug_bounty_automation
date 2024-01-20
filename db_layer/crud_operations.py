import psycopg2
import os


class Crud_operations:
    """Class for CRUD operations"""

    def __init__(self) -> None:
        """Init Crud_operations class"""
        self.dname = os.environ.get("POSTGRES_DB")
        self.user = os.environ.get("POSTGRES_USER")
        self.password = os.environ.get("POSTGRES_PASSWORD")
        self.host = os.environ.get("POSTGRES_HOST")
        self.port = os.environ.get("POSTGRES_PORT")
        self.conn = psycopg2.connect(
            database=self.dname,
            port=self.port,
            user=self.user,
            password=self.password,
            host=self.host,
        )
        self.cur = self.conn.cursor()

    def commit_alterations(self) -> None:
        """execute commit"""
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def insert_subs(self, domain: str, subdomains: list[str], tool: str) -> None:
        """Insert into domain and subdomains table

        Args:
            domain (str): domain name
            subdomains (list[str]): list of subdomains
            tool (str): tool name
        """

        print(type(subdomains))

        self.cur.execute(f"INSERT INTO domains name VALUES ({domain});")

        self.commit_alterations()

        domain_id = self.cur.execute(f"SELECT id FROM domains WHERE name = {domain};")

        list_data = []

        for subdomain in subdomains:
            list_data.append((subdomain, domain_id, tool))

        for data in list_data:
            self.cur.execute(
                f"INSERT INTO subdomains (name, domain_id, tool) VALUES ({data[0]},{data[1]}, {data[2]});"
            )

        self.commit_alterations()
