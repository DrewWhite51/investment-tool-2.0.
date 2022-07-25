import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Saunderscooke51!",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")


def select_query(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        mobile_records = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
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


def compare_watchlist(list_of_tickers):
    first_set = set(list_of_tickers)
    db_arr = []

    for db_tickers in (select_query('select * from investment_tool.watch_list')):
        db_arr.append(db_tickers[0])

    for differences in first_set.difference(db_arr):
        print(f'Adding {differences} to the database.')
        insert_into_watchlist(differences)


def insert_into_daily_stock(ticker):
    pass


def insert_into_hourly_stock(ticker):
    pass


def insert_into_minute_stock(ticker):
    pass


def insert_into_30m_stock(ticker):
    pass


def insert_into_hourly_crypto(ticker):
    pass


def insert_into_daily_crypto(ticker):
    pass


def insert_into_minute_crypto(ticker):
    pass