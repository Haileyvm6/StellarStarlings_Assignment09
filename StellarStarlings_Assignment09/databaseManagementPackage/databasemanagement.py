# databaseManagement.py
# File Name : databasemanagement.py
# Student Name: Hailey Manuel, Liam Vasey , Nate Hoang
# email: manuelhv@mail.uc.edu, vaseylh@mail.uc.edu , hoangnd@mail.uc.edu
# Assignment Number: Assignment 08 
# Due Date: 03/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment involves connecting to a SQL Server, executing queries to retrieve product data, and outputting relevant information.

# Brief Description of what this module does: This module manages the connection to the SQL Server database, submits SQL queries, fetches data, and includes methods for opening and closing the database connection.
# Citations: We used each other, online resources, and class slides for creating methods for connecting to the database and submitting SQL queries.

import pyodbc
from modelsPackage.models import Product

class DatabaseManagement:
    def connect_to_database(self):
        '''
        Connect to our SQL Server instance
        @return the connection object or None on failure 
        '''
        try:
            conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                'Database=GroceryStoreSimulator ;'
                'uid=IS4010Login;'
                'pwd=P@ssword2;'
            )
        except:
            return None
        return conn

    def submit_sql_to_server(self, conn, sql_statement):
        '''
        Submit a SQL statement to our SQL Server
        @param conn: The connection object
        @param sql_statement: The SQL query to execute
        @return: The pyodbc cursor object that contains the query results
        '''
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        return cursor

    def get_random_product(self, conn):
        """Fetch a random product from tProduct."""
        query = "SELECT ProductID, Description, ManufacturerID, BrandID FROM tProduct ORDER BY NEWID()"
        cursor = self.submit_sql_to_server(conn, query)
        row = cursor.fetchone()
        return Product(*row) if row else None

    def get_manufacturer(self, conn, manufacturer_id):
        """Retrieve manufacturer name from tManufacturer."""
        query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        cursor = self.submit_sql_to_server(conn, query)
        row = cursor.fetchone()
        return row[0] if row else "Unknown"

    def get_brand(self, conn, brand_id):
        """Retrieve brand name from tBrand."""
        query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        cursor = self.submit_sql_to_server(conn, query)
        row = cursor.fetchone()
        return row[0] if row else "Unknown"

    def get_items_sold(self, conn, product_id):
        """Calculate total items sold from tTransactionDetail."""
        query = f"SELECT SUM(QtyOfProduct) FROM tTransactionDetail WHERE ProductID = {product_id}"
        cursor = self.submit_sql_to_server(conn, query)
        row = cursor.fetchone()
        return row[0] if row else 0

    def close_connection(self, conn):
        try:
            conn.close()
     
        except Exception as e:
            print(f"Error closing the connection: {e}")