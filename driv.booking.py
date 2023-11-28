import sqlite3 as sq
from sqlite3 import Error

def database_connection():
        try:
            connection = sq.connect(database="sample.db")
            connection.cursor()

            sql_task = """        
            CREATE TABLE BOOKINGS
            (ID INT PRIMARY KEY NOT NULL,
            PICKUP TEXT NOT NULL,
            DROPOFF TEXT NOT NULL,
            COST INT);
            
            CREATE TABLE EMPLOYEES
            (id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL,);
          
            CREATE TABLE Customer Registration
            (customer_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100),
            phone_number INT,
            address VARCHAR(200),
            Username TEXT,
            Password TEXT);
            
            CREATE TABLE Driver_Verification (
            Driver_Permit VARCHAR(10),
            Drivers_Insurance TEXT,
            Vehicle_Inspection VARCHAR(10),
            Vehicle_Number VARCHAR(6)
            );
         """

            response = connection.execute(sql_task)


        except Exception as error_code:
            raise error_code
