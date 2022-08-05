"""Read a CSV file"""
import csv

f = open('employees.txt', encoding='utf-8')
csv_file = csv.reader(f)
for row in csv_file:
    name, phone, role = row
    print(f"Name: {name}, Phone: {phone}, Role: {role}")
f.close()
