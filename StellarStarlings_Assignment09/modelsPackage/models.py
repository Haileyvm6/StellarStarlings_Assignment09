# models.py
# File Name : models.py
# Student Name: Hailey Manuel, Liam Vasey , Nate Hoang
# email: manuelhv@mail.uc.edu, vaseylh@mail.uc.edu , hoangnd@mail.uc.edu
# Assignment Number: Assignment 09 
# Due Date: 03/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment involves connecting to a SQL Server, executing queries to retrieve product data, and outputting relevant information.

# Brief Description of what this module does: This module defines the Product class, which represents a product with attributes like ProductID, Description, ManufacturerID, and BrandID, used in the main program for database queries and data manipulation.
# Citations: We used each other, online resources, and class slides for designing the structure of the Product class and its attributes.


class Product:
    def __init__(self, product_id, description, manufacturer_id, brand_id):
        self.product_id = product_id
        self.description = description
        self.manufacturer_id = manufacturer_id
        self.brand_id = brand_id
