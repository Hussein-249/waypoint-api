import psycopg2
import os


class PostgresSetup:
    def __init__(self, dbname):
        self.name = dbname

    @staticmethod
    def execute_sql_file(sql_filename: str, connection):
        try:
            cur = connection.cursor()
            with open(sql_filename, 'r') as file:
                sql_query = file.read().split(';') # NOT OPTIMAL, file.read() loads entire file into memory
                # needs to be optimized
                for query in sql_query:
                    if query.strip():
                        cur.execute(query)
            connection.commit()
            cur.close()
        except Exception as e:
            print(f'Exception occurred during reading an SQL file:\n{e}')

        return

    def connect_postgres_database(self):
        try:
            postgres_connection = psycopg2.connect(database=self.name, user="postgres",
                                                   password="postgres", host="localhost",
                                                   port="5432")
            postgres_connection.autocommit = True

            return postgres_connection

        except Exception as e:
            print("An error occurred whilst attempting to create the database."
                  f"\n Exception: {e}")
            return None


def create_table(table_name: str, connection):
    try:
        cur = connection.cursor()

        cur.execute("SELECT current_database()")

        db_name = cur.fetchone()

        print(f"Connection established with database: {db_name}")

        create_canada = (
            f"CREATE TABLE {table_name}"
            "(wpname varchar(5) PRIMARY KEY,lat varchar(25) NOT NULL, lon varchar(25) NOT NULL)"
        )

        cur.execute(create_canada)

        cur.close()

        print(f"{table_name} created in {db_name}")

    except Exception as e:
        print("Connection valid, but an error occurred during table creation."
              f"Exception: {e}")


def add_from_csv(filename: str, connection):

    cur = connection.cursor()

    with open(filename, newline='\n') as csv_file:

        copy_data = """
                COPY CanadaWaypoints(wpname, lon, lat) FROM stdin WITH CSV HEADER
                DELIMITER as ','
                """

        cur.copy_expert(sql=copy_data, file=csv_file)

        connection.commit()

        cur.close()


postgresHandler = PostgresSetup("postgres")

conn = postgresHandler.connect_postgres_database()

create_table("CanadaWaypoints", conn)

# add_from_csv("../resources/CANADA_WAYPTS.csv", conn)
add_from_csv("CANWAYPOINTS.csv", conn)
conn.close()
