import mysql.connector
from mysql.connector import Error

hostname = "127.0.0.1"
username = "root"
password = "nani1318"
database = "my_db"  

connection = None

try:
    # Establishing the connection
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_Info}")

        # Creating a cursor object to execute queries
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record[0]}")

        create_student_table_query = '''
        CREATE TABLE IF NOT EXISTS Student (
            id INT PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(40),
            date_of_birth DATE
        )
        '''
        cursor.execute(create_student_table_query)
        print("Table 'Student' created successfully.")

        # Optional: Verify table creation
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])
    else:
        print("Failed to connect to MySQL database")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    # Closing the cursor and connection
     # Closing the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

