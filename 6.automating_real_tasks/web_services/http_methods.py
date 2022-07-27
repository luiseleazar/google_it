import requests

URL = 'https://example.com/path/to/api'
parameters = {"search": "grey kitten",
        "max_results": 15}
response = requests.get(URL, params=parameters)
complete_url = response.request.url 
#Output:'https://example.com/path/to/api?search=grey+kitten&max_results=15'

data = {"description": "white kitten",
        "name": "Snowball",
        "age_months": 6}
response = requests.post(URL, data=data)
body = response.request.body 
#Output: 'description=white+kitten&name=Snowball&age_months=6'
