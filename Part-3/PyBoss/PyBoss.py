# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

# Import required packages
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("raw_data", "employee_data.csv")
file_to_output = os.path.join("analysis", "employee_data_reformatted.csv")

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:

        # Grab emp_ids and store it into a list
        emp_ids = emp_ids + [row[0]]

        # Grab names, split them, and store them in a temporary variable
        split_name = row[1].split(" ")

        # Then save first and last name in separate lists
        emp_first_names.append(split_name[0])
        emp_last_names.append(split_name[1])

        # Grab DOB and reformat it
        split_DOB = row[2].split("-")
        year = split_DOB[0]
        month = split_DOB[1]
        day = split_DOB[2]
        DOB_format = month + "/" + day + "/" + year

        # Then store it into a list
        emp_dobs.append(DOB_format)

        # Grab SSN and reformat it
        split_SSN = row[3].split("-")
        last4 = split_SSN[2]
        SSN_format = "***-**-" + last4
                
        # Then store it into a list
        emp_ssns.append(SSN_format)

        # Grab the states and use the dictionary to find the replacement
        state = row[4]
        state_abbrev = us_state_abbrev[state]

        # Then store the abbreviation into a list
        emp_states.append(state_abbrev)

# Zip all of the new lists together
emp_info = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)

# Write all of the election data to csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter =",")

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(emp_info)