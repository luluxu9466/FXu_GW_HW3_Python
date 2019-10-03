# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os
import pandas as pd 

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
dict = {}
max_month = ""

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    profit = int(next(reader)[1])
    total_months = 1
    total_net = profit

    for row in reader:

        # Track the total
        total_months += 1 
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - profit
        net_change_list.append(net_change)
        profit = int(row[1])
        month_of_change.append(row[0])

    # Calculate the greatest increase
        dict[row[0]] = net_change
    
    max_change = max(net_change_list)
    for key in dict:
        if dict[key] == max_change:
            max_month = key
    greatest_increase = [max_month, max_change]
    # Calculate the greatest decrease
    min_change = min(net_change_list)
    for key in dict:
        if dict[key] == min_change:
            min_month = key
    greatest_decrease = [min_month, min_change]
            
# Calculate the Average Net Change
print(net_change_list)
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
file = open("outputs.txt","w")
file.write(output)