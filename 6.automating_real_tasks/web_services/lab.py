"""
You're working at a company that sells second-hand cars. 
Your company constantly collects feedback in the form of customer reviews. 
Your manager asks you to take those reviews (saved as .txt files) 
and display them on your company's website. 
To do this, you'll need to write a script to convert those .txt files
and process them into Python dictionaries, 
then upload the data onto your company's website (currently using Django).
"""
# NOTE: This lab was hardcoded because of how the dictionaries was bevaving

import os
import requests

text_files = os.listdir('/data/feedback')
file_contents = []

for file in text_files:
    content = ""
    file_path = '/data/feedback/' + file
    with open(file_path, encoding="utf-8") as f:
        content = f.readlines()
    file_contents.append(content)
#print(file_contents)

list_of_dicts = []
print(file_contents[0])
for feedback in file_contents:
    new_dict = {"title":feedback[0].replace('\n',''),
        "name": feedback[1].replace('\n',''),
        "date":feedback[2].replace('\n',''), 
        "feedback":feedback[3].replace('\n','')}
    list_of_dicts.append(new_dict)
    #print(new_dict)
URL = 'http://34.135.20.37'

for feed in list_of_dicts:
    #print(f"Feed to post: {feed}")
    response = requests.post(URL, data=feed)
    if response.ok:
        print('Successful response')
    else:
        print(f'Status code:{response.status_code}')
