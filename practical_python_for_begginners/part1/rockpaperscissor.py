import random #import the 'random' module that randomizes answer

computer_choice = random.choice(['scissor', 'rock', 'paper']) #computer will randomly pick one of three

user_choice = input('do you want - rock paper or scissor?\n')

if computer_choice == user_choice:
    print("tie")
elif user_choice == 'rock' and computer_choice == 'scissor':
    print("you win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("win")
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('win')
else:
    print('loser')