# -*- coding: UTF-8 -*-

import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # YOUR CODE HERE
        email = row["first_name"].lower() + "." + row["last_name"].lower() + "@example.com"
        new_employee_data.append({"first_name": row["first_name"],
        "last_name": row["last_name"], 
        "ssn": row["ssn"],
        "email": email})

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", "employee_email.csv")
with open(csvpath, "w") as csvfile:
    # YOUR CODE HERE
    fieldnames = ['first_name', 'last_name', 'ssn', 'email']
    writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)