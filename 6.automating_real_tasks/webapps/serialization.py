import json
import yaml

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

#JSON
with open('people.json', 'w', encoding="utf-8") as people_json:
    json.dump(people, people_json, indent=2)

people_dict = json.dumps(people) #This returns a string instead of JSON object

with open('people.json', 'r', encoding='utf-8') as people_json:
    people_loaded = json.load(people_json) #Inverse of dump()

#YAML
with open('people.yaml', 'w', encoding='utf-8') as people_yaml:
    yaml.safe_dump(people, people_yaml)
