# main.py
# main.py
# Student Name: Hailey Manuel, Liam Vasey , Nate Hoang
# email: manuelhv@mail.uc.edu, vaseylh@mail.uc.edu , hoangnd@mail.uc.edu
# Assignment Number: Assignment 09 
# Due Date: 03/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment involves connecting to a SQL Server, executing queries to retrieve product data, and outputting relevant information.

# Brief Description of what this module does: This module connects to the database, fetches a random product's details, retrieves the manufacturer and brand information, calculates the total number of items sold, and displays this data in a formatted sentence.
# Citations: We used each other, online resources, and class slides for assistance in troubleshooting and structuring the database connection and queries.

import random
from databaseManagementPackage.databasemanagement import DatabaseManagement
from modelsPackage.models import Product

dbm = DatabaseManagement()

conn = dbm.connect_to_database()

if conn:
       query = 'SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM dbo.tProduct'
       cursor = dbm.submit_sql_to_server(conn, query)
       products = cursor.fetchall()

       if not products:
         print("No products found.")
       else:
         selected_product = random.choice(products)
         product = Product(
            product_id=selected_product.ProductID,
            description=selected_product.Description,
            manufacturer_id=selected_product.ManufacturerID,
            brand_id=selected_product.BrandID
        )
