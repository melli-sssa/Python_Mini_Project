def check_winner(p1_hp, cpu_hp):
    if cpu_hp <= 0:
        print("Player 1 Wins!")
        return True

    elif p1_hp <= 0:
        print("CPU Wins!")
        return True

    return False
