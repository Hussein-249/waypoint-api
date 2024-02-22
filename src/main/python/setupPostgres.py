import psycopg2


def create_database(name: str):
    print("CREATING NEW DATABASE")

    try:
        postgres_connection = psycopg2.connect(database="postgres", user="postgres",
                                               password="postgres", host="localhost",
                                               port="5432")
        postgres_connection.autocommit = True

        # dbcursor = postgres_connection.cursor()

        # postgres_query = '''CREATE database ''' + name

        # dbcursor.execute(postgres_query)

        # print(name + " created")

        # dbcursor.close()
        #
        # postgres_connection.close()

        # postgres_connection2 = psycopg2.connect(database=name, user="postgres",
        #                                         password="postgres", host="localhost",
        #                                         port="5432")

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
            "(wpname varchar(5) PRIMARY KEY,lat varchar(20) NOT NULL, lon varchar(20) NOT NULL)"
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
                COPY canada(wpname, lon, lat) FROM stdin WITH CSV HEADER
                DELIMITER as ','
                """

        cur.copy_expert(sql=copy_data, file=csv_file)

        connection.commit()

        cur.close()


conn = create_database("Waypoints")

create_table("Canada", conn)

add_from_csv("../resources/cantemp.csv", conn)

conn.close()
