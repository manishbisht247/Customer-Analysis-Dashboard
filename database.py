import mysql.connector
import pandas as pd
import queries
def connect():
    try:
        connection = mysql.connector.connect(
            host = 'mysql-39e1b56e-customer-analysis.l.aivencloud.com',
            user = 'avnadmin',
            password = 'YOUR AIVEN PASSWORD',
            database = 'customer',
            port = 21411,
            ssl_ca = r"C:\Users\mbvin.BEEST7PC\Downloads\ca.pem"
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

