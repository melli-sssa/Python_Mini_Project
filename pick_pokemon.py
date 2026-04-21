
import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)

pokemon_list = json.loads(response.text)['results']
pokemon_data = json.loads(response.text)['results']


# Get the pokemons data from API
def pick_pokemon():

    x = 1

    for pokemon in pokemon_list:
        print (f" {x}.{pokemon['name']}")
        x +=1
    return pokemon_list

# present pokemon list
pick_pokemon()

# Ask the user to choose a pokemon
print('Enter your pokemon:')


# Get the user's choice
choice = input().lower()

selected_pokemon = None
for pokemon in pokemon_list:
    if pokemon['name'] == choice:
        selected_pokemon = pokemon
        break

if selected_pokemon is None:
    print("Pokemon not found")
else:
    response = requests.get(selected_pokemon['url'])
    pokemon_data = json.loads(response.text)

    # to get ability & health
    abilities = pokemon_data['abilities'][0]
    ability = abilities['ability']
    health = 100

    # to format height and weight properly
    height = int(pokemon_data['height'])
    weight = int(pokemon_data['weight'])

    height_formatted = height / 10
    weight_formatted = weight / 10

    # Print the pokemon's data
    print('Name: {}'.format(pokemon_data['name']))
    print('Weight: {}'.format(weight_formatted) + "(kgs)")
    print('Height: {}'.format(height_formatted) + "(m)")
    print('Ability: {}'.format(ability['name']))
    print('Health: {}'.format(health))