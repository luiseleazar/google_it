import requests
import os

path = '~/supplier-data/images/'
image_list = os.listdir(path)
ip = ''
url = 'http://' + ip + '/upload/'

for image in image_list:
    if image.endswith("jpeg"):
        with open(path + image, 'rb') as opened:
            response = requests.post(url, files={'file':opened})
