import requests

response = requests.get('https://www.google.com')

if response.ok:
    print('The request was OK')
else:
    raise Exception(f"GET failed with status code: {response.status_code}")
