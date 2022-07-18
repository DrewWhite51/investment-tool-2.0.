import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Saunderscooke51!",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")


def print_connection():
    return connection


def select_query():
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = 'select * from "endurance-trainer".workouts;'
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return mobile_records


def insert_query(query):
    pass


def delete_query(query):
    pass


def update_query(query):
    pass