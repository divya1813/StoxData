from project import *
import sqlite3
import pandas as pd

def connect_to_database():
    return sqlite3.connect('stocks.db')

def insert_data(conn, Company_ID, Ticker, Open, High, Low, Close, Adjclose, Volume):
    query = '''
        INSERT INTO Stocks (Company_ID, Ticker, Open, High, Low, Close, Adjclose, Volume)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    conn.execute(query, (Company_ID, Ticker, Open, High, Low, Close, Adjclose, Volume))
    conn.commit()

def select_data(conn):
    query = 'SELECT * FROM Stocks'
    result = pd.read_sql_query(query, conn)
    return result

def update_data(conn, Company_ID, New_Company):
    query = 'UPDATE Stocks SET Ticker=?  WHERE Company_ID=?'
    conn.execute(query, (New_Company, Company_ID))
    conn.commit()

def delete_data(conn, Company_ID):
    query = 'DELETE FROM Stocks WHERE Company_ID=?'
    conn.execute(query, (Company_ID,))
    conn.commit()