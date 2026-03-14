import random
import os
import math
from art import *

lives = 0
def difficulty_select():
    global lives
    while True:
        difficulty = input("Choose a difficulty. Type 'Hard' or 'Easy':\n").lower()
        if difficulty == "easy":
            lives = 10
            break

        elif difficulty == "hard":
            lives = 5
            break

        else:
            print("Please enter a valid input")
def random_number():
    
    return random.randint(0,100)
def play_game():
    print(logo)
    global lives
    difficulty_select()
    number = random_number()

    while lives != 0:

        try:
            print(f"Lives left: {lives}")
            guess = int(input("Enter your guess: "))
            
            if guess > number and math.isclose(number,guess, abs_tol= 10) == True:
                print("Warmer but go lower")
                lives -= 1

            elif guess < number and math.isclose(number,guess, abs_tol= 10) == True:
                print("Warmer but go higher")
                lives -= 1
                
            elif guess > number:
                print("Go Lower")
                lives -= 1

            elif guess < number:
                print("Go Higher")
                lives -= 1

            elif guess == number:
                break

        except ValueError:
            print("Please enter a proper number")

    if guess == number:
        print(win)
    
    else:
        print(loose) 

while input("Do you want to play a game of number guessing? (enter 'y' for yes and enter for no)").lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()