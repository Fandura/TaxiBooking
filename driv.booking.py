import sqlite3  # Import the SQLite library

def database_connection():
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect("sample.db")

        if connection:
            print("Connected to the database!")

            # Create a cursor object to execute queries
            cursor = connection.cursor()

            # Return both the connection and cursor objects
            return connection, cursor

    except sqlite3.Error as error:
            print("Error connecting to the database:", error)
            return None, None  # Return None if connection fails

            # SQL Booking tasks
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
            
            CREATE TABLE Driver_Preview (
            Driver_designated_trips TEXT INT PRIMARY KEY,
            Driver_fully_booked_trips TEXT
            );
);
         """

            response = connection.execute(sql_task)


    except Exception as error_code:
            raise error_code
