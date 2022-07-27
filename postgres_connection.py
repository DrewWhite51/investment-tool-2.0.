import psycopg2
import time
import os
import csv

connection = psycopg2.connect(user="postgres",
                              password="Saunderscooke51!",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")


def write_daily_ohlc(stock_obj):
    stock_obj.get_daily_technicals().iloc[1:].to_csv(f'{stock_obj.get_ticker()}.csv')

    file = f'{stock_obj.get_ticker()}.csv'

    query = """
    INSERT INTO investment_tool.ibm_daily_ohlc(
	ticker, date, open, high, low, close)
	VALUES (?, ?, ?, ?, ?, ?);
    """

    try:
        cursor = connection.cursor()
        with open(file, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                print(row)
                cursor.execute(query, (row[0], row[1], row[2], row[4], row[3],))

        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if connection:
            cursor.close()

    os.remove(f'{stock_obj.get_ticker()}.csv')


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
