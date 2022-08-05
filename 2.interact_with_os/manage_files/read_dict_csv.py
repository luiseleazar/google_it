"""Read CSV file with title in columns"""
import csv

with open("software.csv", 'r', encoding='utf-8') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))
