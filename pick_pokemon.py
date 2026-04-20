
import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

x = 1
for pokemon in pokemon_list:
    print (f" {x}.{pokemon['name']}")
    x +=1


