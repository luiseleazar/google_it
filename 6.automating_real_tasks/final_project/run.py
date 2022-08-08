#!/usr/bin/env python3
import os
import requests
import json

ip = ''
url = 'http://' + ip + '/fruits'

def public_fruits(f):
    """Public fruits on web page"""
    with open(f, 'r', encoding='utf-8') as txt:
        name = txt.readline()
        weight = txt.readline()
        description = txt.readline()
    image = f.split("/")
    image = image[-1].replace("txt","jpeg")
    weight = int(weight.replace("lbs", ""))
    request_body = {"name": name[:-1],
        "weight": weight,
        "description": description.strip(),
        "image_name": image}
    #TODO: Check why dictionary gets ' and not "", that the reason of getting failed requests
    print(request_body)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data = json.dumps(request_body))
    if response.status_code != 200:
        print('Request failed')
        print(f"Status code: {response.status_code}")

#Path of txt files
path = 'supplier-data/descriptions/'
file_list = os.listdir(path)

for file in file_list:
    if file.endswith('txt'):
        public_fruits(path + file)
