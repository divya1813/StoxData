import pandas as pd
import sqlite3

# Replace 'your_file.csv' with the path to your CSV file
database_file = 'stocks.db'

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(r"C:\Users\vani\Downloads\stocks.csv", header=0)

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect(database_file)

# Write DataFrame to SQLite database
df.to_sql('Stocks', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('stocks.db')


# Read data from the SQLite table
df_from_db = pd.read_sql_query('SELECT * FROM Stocks', conn)

# Display the DataFrame
print(df_from_db.head())

# Close the connection
conn.close()