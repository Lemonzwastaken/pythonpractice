from game_data import *
import random
from art import*
import os

data1 = random.choice(data)

game_running = True
score = 0

while game_running:
    data2 = random.choice(data)   
    print(f"{logo}")
    print(f"Compare A: Name: {data1['name']}\nDescription: A {data1['description']}\nLocation: {data1['country']}")
    print(f"{vs}")
    print(f"Compare with B: Name: {data2['name']}\nDescription: A {data2['description']}\nLocation: {data2['country']}")


    while True:
        guess = input("Who has more followers? Type A or B:  ").lower()
        if guess == 'a':
            if data1['follower_count'] > data2['follower_count']:
                os.system('cls' if os.name=='nt' else 'clear')
                print("CORRECT!!!")
                score += 1
                print(f"Score = {score}")


            else:
                game_running = False
            
            break

        elif guess == 'b':
            if data2['follower_count'] > data1['follower_count']:
                os.system('cls' if os.name=='nt' else 'clear')
                print("CORRECT!!!")
                score +=1 
                print(f"Score = {score}")
                data1 = data2

            else:
                os.system('cls' if os.name=='nt' else 'clear')
                game_running = False
            
            break

        else:
            print("Choose either A or B")

game_over(score)

