def player_move(pokemon: object) -> None:

    print("--------------- It's your turn ! ---------------- \n")

    print("Possible moves: \n")
    print(f"1. {pokemon["moves"][0]}")
    print(f"2. {pokemon["moves"][1]}")
    print(f"3. {pokemon["moves"][2]}")

    player_choice = ""

    while player_choice not in (1, 2, 3):
        player_choice = int(input("Choose your next move: (1, 2, 3)"))

    print(f"{pokemon["name"]} uses {pokemon["moves"][player_choice - 1]}")