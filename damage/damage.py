import random

def damage_taken(pokemon: object) -> int:

    ability_damage = random.randint(5, 20)

    print(f"\n It does {ability_damage} damage !")

    pokemon["hp"] -= ability_damage

    print(f"\n {pokemon["name"]} has {pokemon["hp"]} left !")

    return pokemon["hp"]
