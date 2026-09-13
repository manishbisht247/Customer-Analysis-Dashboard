import mysql.connector
import pandas as pd
import queries
def connect():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'customer'
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

