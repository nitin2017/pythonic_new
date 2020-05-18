# EXERCISE , NUMBERING GAME
# Make a variable winning_number and assign any value to it
# Ask user to guess a number 
# if user guessed correctly print "YOU WIN !!!"
# if user didn't guessed correctly :
#     if user guessed lower than the actual number then print "TOO LOW"
#     if user guessed greater than the actual number then print "TOO HIGH"

import random
winning_number = random.randint(1,101)
guess = 1
game_over = False
user_number = int(input("Enter your number between 1 and 100 :- ").strip())
while not game_over:
    if user_number == winning_number:
        print("YOU WON")
        print(f"YOU GUESSED THIS IN {guess} TIMES")
        game_over = True
    else:
        if user_number<winning_number:
            print("TOO LOW")
        else:
            print("TOO HIGH")
        guess += 1
        user_number = int(input("Guess again number between 1 and 100 :- ").strip())
