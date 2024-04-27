import psycopg2
from psycopg2.extras import RealDictCursor


def db_connect(dbname="postgres"):
    try:
        postgres_connection = psycopg2.connect(database=dbname, user="postgres",
                                               password="postgres", host="localhost",
                                               port="5432")
        postgres_connection.autocommit = True

        return postgres_connection

    except Exception as e:
        print("An error occurred whilst attempting to connect to the specified database."
              f"\n Exception: {e}")
        return None


def query_single_point(waypoint, connection):
    try:

        cur = connection.cursor(cursor_factory=RealDictCursor)

        query_string = f"SELECT * FROM canada WHERE wpname = %s"    # don't directly include variables in query

        cur.execute(query_string, (waypoint,))  # prevent SQL injection attacks

        res = cur.fetchone()

        cur.close()

        db_disconnect(connection)

        return res

    except Exception as e:
        print("Unable to execute query or find waypoint."
              f"\n Exception: {e}")


def find_shortest_route(origin, destination, connection):
    # DOES NOT WORK
    # need to implement typechecking, changes based on whether coord, name, or waypt
    cur = connection.cursor(cursor_factory=RealDictCursor)

    all_points_between = f"SELECT * FROM canada WHERE wpname = %s"    # don't directly include variables in query

    origin_query = f"SELECT lon, lat FROM canada WHERE wpname = %s"  # don't directly include variables in query

    destination_query = f"SELECT lon, lat FROM canada WHERE wpname = %s"

    cur.execute(destination_query, (destination,))

    # res = cur.fetchall()
    res = "Results"
    return res


def db_disconnect(connection):
    connection.close()
