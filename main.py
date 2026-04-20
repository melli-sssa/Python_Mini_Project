
from player_choosing_ability.player_move import player_move

from check_winner import check_winner
from cpu_player import cpu_player

if __name__ == '__main__':
    # player_pokemon = Melissa player choosing pokemon

    cpu_pokemon = cpu_player()

    # return {
    #     "name": pokemon_name,
    #     "hp": 100,
    #     "id": pokemon_id,
    #     "abilities": pokemon_abilities
    # }

    # while not check_winner(player_pokemon["health"], cpu_pokemon["health"]):
    #     player_move(player_pokemon)
    #     if check_winner(player_pokemon["health"], cpu_pokemon["health"]):
    #         break
    player_move(cpu_pokemon, user_turn = False)


