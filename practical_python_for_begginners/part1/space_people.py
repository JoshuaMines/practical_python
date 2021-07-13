import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('the people currently in spce are')
for person in json['people']:
    print(person['name'])