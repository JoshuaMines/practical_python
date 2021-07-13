import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("enter player 1's name:")
    player2 = input("enter player 2's name:")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rolled", roll1)
    print(player2, "rolled", roll2)

    if roll1 > roll2:
        print('player 1 wins')
    elif roll2 > roll1:
        print('player 2 wins')
    else:
        print('you tie!')

main()