"""Generate a CSV file based on a list of dictionaries with title columns"""
import csv

users = [{"name":"Sol Mansi", "username":"solm", "department": "IT Infrastructure"},
        {"name":"Lio Nelson", "username":"lion", "department": "User Experience Research"},
        {"name":"Charlie Grey", "username":"greyc", "department": "Development"}]

keys = ["name", "username", "department"]
with open("by_department.csv", 'w', encoding='utf-8') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
