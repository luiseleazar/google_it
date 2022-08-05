"""Generate a CSV file based on a list of list"""
import csv

HOSTS = [["workstation.local", "192.168.25.46"], ["webserver", "10.2.5.6"]]

with open("hosts.csv", 'w', encoding='utf-8') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(HOSTS)
