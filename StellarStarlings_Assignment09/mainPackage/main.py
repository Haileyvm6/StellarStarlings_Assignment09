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
 
       manufacturer_query = f"SELECT Manufacturer FROM dbo.tManufacturer WHERE ManufacturerID = {product.manufacturer_id}"
       cursor = dbm.submit_sql_to_server(conn, manufacturer_query)
       manufacturer = cursor.fetchone()
       manufacturer_name = manufacturer[0] if manufacturer else "Unknown"

       
       brand_query = f"SELECT Brand FROM dbo.tBrand WHERE BrandID = {product.brand_id}"
       cursor = dbm.submit_sql_to_server(conn, brand_query)
       brand = cursor.fetchone()
       brand_name = brand[0] if brand else "Unknown"

       
       sales_query = f"""
            SELECT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
            FROM dbo.tTransactionDetail 
            INNER JOIN dbo.tTransaction 
            ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
            WHERE dbo.tTransaction.TransactionTypeID = 1 
            AND dbo.tTransactionDetail.ProductID = {product.product_id}
        """
       cursor = dbm.submit_sql_to_server(conn, sales_query)
       items_sold = cursor.fetchone()
       total_sold = items_sold[0] if items_sold[0] is not None else 0

        
       final_sentence = (f"The product '{product.description}' is manufactured by '{manufacturer_name}', "
                          f"under the brand '{brand_name}', and has sold {total_sold} units.")
       print(final_sentence)

    
       dbm.close_connection(conn)
else: 
     None

