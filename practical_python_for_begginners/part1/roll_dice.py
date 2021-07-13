import random

roll = random.randint(1,6)

guess = int(input('guess the dice roll:\n'))

if guess == roll:
    print("corrct! they rolled a " + str(roll))
else:
    print("wrong")