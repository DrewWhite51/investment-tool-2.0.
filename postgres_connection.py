import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Saunderscooke51!",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")


def print_connection():
    return connection


def select_query(query):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = query
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()

    return mobile_records


def insert_into_watchlist(ticker):
    try:
        cursor = connection.cursor()
        insert_statement = 'INSERT INTO investment_tool.watch_list(ticker) VALUES (%s);'
        args = ticker
        cursor.execute(insert_statement, (args,))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
    return None


def delete_query(query):
    pass


def update_query(query):
    pass