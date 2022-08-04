import requests
import os

ip = ''
url = 'http://' + ip + '/fruits'

def public_fruits(f):
    with open(f, 'r', encoding='utf-8') as txt:
        name = txt.readline()
        weight = txt.readline()
        description = txt.readline()
    image = f.split("/")
    image = image[-1].replace("txt","jpeg")
    weight = int(weight.replace("lbs", ""))
    request_body = {"name": name[:-1],
        "weight": weight,
        "description": description,
        "image_name": image}
    print(request_body)
    response = requests.post(url, data = request_body)
    if response.status_code != 200:
        print('Request failed')

#Path of txt files
path = '~/supplier-data/descriptions/'
file_list = os.listdir(path)

for file in file_list:
    if file.endswith('txt'):
        public_fruits(path + file)
