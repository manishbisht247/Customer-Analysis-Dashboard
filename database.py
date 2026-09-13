import mysql.connector
import pandas as pd
import queries
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    try:
        connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                ssl_ca=os.getenv("DB_SSL_CA")
            )
        return connection
    except mysql.connector.Error() as error:
        print(f"MySQL connection Error: {error}")
        return None

if __name__ == "__main__":
    connection = connect()
    cursor = connection.cursor(buffered = True)

    customers = queries.get_customers(cursor, country = 'india', gender = 'feMALE', minAge=12, maxAge=18)
    for cust in customers:
        print(cust)


    cursor.close()
    connection.close()

