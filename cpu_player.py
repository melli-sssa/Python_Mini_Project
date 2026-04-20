import random
import requests

def cpu_player():

    random_id = random.randint(1, 20)

    # 2. Construct the API URL using that ID
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

    try:
        # Use 'requests' to fetch the data from the PokéAPI
        response = requests.get(url)

        # Check if the "handshake" with the server was successful
        if response.status_code == 200:
            data = response.json()

            # Extract only the pieces we need: Name and ID
            pokemon_name = data['name'].capitalize()
            pokemon_id = data['id']
            pokemon_abilities = []

            for ability in data['abilities']:
                pokemon_abilities.append(ability["ability"]['name'])

            print(f"\n Selection Complete! CPU chose: {pokemon_name} (National Dex #{pokemon_id})")

            # Return stats as dictionary
            return {
                "name": pokemon_name,
                "hp": 100,
                "id": pokemon_id,
                "abilities": pokemon_abilities
            }

        else:
            print("Failed to find pokemon")

    except Exception as e:
        print(f"An error occurred: {e}")
