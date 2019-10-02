import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])

        # Add amount of reviews
        reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
        reviewpctg =  str(round(int(row[6])/int(row[5]) * 100, 2))
        review_percent.append(reviewpctg)

        # Get length of the course to just a number
        length_str = row[9]
        length_num = float(length_str.strip(" hoursmins"))

        if length_str[-4] == "m":
            length_num = length_num / 60
        unit = length_str.strip(" ")[1]

        length.append(length_num)

# Zip lists together
udemy_zip = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter =",")

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(udemy_zip)
