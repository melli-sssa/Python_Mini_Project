import random
from damage.damage import damage_taken

def player_move(pokemon: object, user_turn = True) -> None:
    if user_turn:
        print("\n--------------- It's your turn ! ---------------- \n")
    else:
        print("\n--------------- CPU's turn, please wait ! ---------------- \n")

    print(f"Possible moves for {pokemon['name']}:")

    num_abilities = len(pokemon["abilities"])

    for i in range(num_abilities):
        print(f"{i+1}. {pokemon['abilities'][i]}")

    player_choice = ""

    if user_turn:
        while player_choice not in (1, 2, 3):
            player_choice = int(input("Choose your next move: (1, 2, 3)"))

    else:
        player_choice = random.randint(1, num_abilities)

    print(f"{pokemon['name']} uses {pokemon['abilities'][player_choice - 1]}")
    # Function to damage using random