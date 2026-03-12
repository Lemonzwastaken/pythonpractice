import random
import os
import time
from art import *
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

plays = 1

def deal_cards(card_list):
    """Deals a random card to the player and adds it to their total"""

    card = random.choice(cards)
    if card == 11:   #Checks for an ace
        if sum(cards) + card > 21:
            card_list.append(1)
        else:
            card_list.append(11)
  
    else:   #if no ace
        card_list.append(card)

def play_game():

    global plays
    

    game_running = True
    player_cards = []
    computer_cards = []

    print("Dealing cards.....please wait")
    time.sleep(5)
    
    for i in range(2):
        deal_cards(card_list=player_cards)
        deal_cards(card_list=computer_cards)

    #GAME LOOP
    while game_running:
        print("\n"*2)
        print(f"Game Number: {plays}\n")
        print(f"Computer's first card = {computer_cards[0]}")
        print(f"Your cards are: {player_cards}")
        print(f"Player_score = {sum(player_cards)}")

        choice = input("Do you wanna deal another set of cards('y' for yes, 'n' for no): \n").lower()
        if choice == "y":

            print("Dealing cards.....please wait")
            time.sleep(5)
            if sum(computer_cards) < 17:
                deal_cards(card_list=computer_cards)

            deal_cards(card_list=player_cards)
            if sum(player_cards) >= 21 or sum(computer_cards) >= 21:
                game_running = False

        elif choice == "n":
            while sum(computer_cards) < 17:
                deal_cards(card_list=computer_cards)
            
            game_running = False

    plays += 1
    print("FINAL EVALUATION:")
    print(f"Computer's cards = {computer_cards}")
    print(f"Your cards are: {player_cards}")
    print(f"Player_score = {sum(player_cards)}")

    if input("press enter to continue") == "Booga":
        print("BAAAHAHHAHAHA")


    os.system('cls' if os.name=='nt' else 'clear')

    computer_total = sum(computer_cards)
    player_total = sum(player_cards)

    if player_total > 21:
        computer_win(player=player_total, computer=computer_total)

    elif computer_total > 21:
        player_win(player=player_total, computer=computer_total)

    elif player_total == 21:
        if computer_total == 21:
                computer_win(player=player_total, computer=computer_total)
        else:
                player_win(player=player_total, computer=computer_total)
        
    elif computer_total == 21:
        computer_win(player=player_total, computer=computer_total)

    elif computer_total > player_total:
        computer_win(player=player_total, computer=computer_total)

    elif player_total > computer_total:
        player_win(player=player_total, computer=computer_total)

    elif player_total == computer_total:
        tie(player=player_total, computer=computer_total)

while input("Do you wish to play another game of blackjack('y' for yes, 'n' for no):\n") == 'y':
    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)
    play_game()