import random

guess = 0

computer_number = random.randint(1,100)

name = input("hey what is your name?")

print("hey there", name, "I'm thinking of a number between 1 and 100")

while guess < 100:
    number = int(input('guess a number!'))    
    guess = guess + 1

    if number > computer_number:
        print("Your guess is too high, try again")
    elif number < computer_number:
        print("Your guess is too low, try again")
    elif number == computer_number:
        break 

if number == computer_number:
    print('good job' + name + 'you got the correct answer in' + guess + 'guesses')







       



