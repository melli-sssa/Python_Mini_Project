import random
import requests

def cpu_player():
    # 1. The CPU picks a random ID (1 to 20 represents all known Pokémon)
    # This is like the CPU closing its eyes and pointing at a list.
    random_id = random.randint(1, 20)

    # 2. Construct the API URL using that ID
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

    try:
        # 3. Use 'requests' to fetch the data from the PokéAPI
        response = requests.get(url)

        # 4. Check if the "handshake" with the server was successful
        if response.status_code == 200:
            data = response.json()

            print(data)

            # 5. Extract only the pieces we need: Name and ID
            pokemon_name = data['name'].capitalize()
            pokemon_id = data['id']

            print(f"Selection Complete! CPU chose: {pokemon_name} (National Dex #{pokemon_id})")

            # Return stats as dictionary
            return {
                "name": pokemon_name,
                "hp": 100,
                "id": pokemon_id
                #"ability_1":data
               # "ability_2"
            }


        else:
            print("Failed to find pokemon")

    except Exception as e:
        print(f"An error occurred: {e}")


cpu_player()