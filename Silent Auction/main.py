from art import *
from functions import *

while True:
    try:
        biddingtype = int(input("Which type of bidding do you wanna undertake\n(1)Normal Bidding: See all bidders and their bids" \
        "\n(2)Incognito Bidding: No access to anyone's bids or names" \
        "\n(3)Random Bid: Complete random bid, all luck of game"
        "\nSelection: "))
        
        if biddingtype == 1:
            normal_auction()
        elif biddingtype == 2:
            silent_auction()
        elif biddingtype == 3:
            random_auction()
        break
    
    except ValueError:
        print("Please enter a valid token")    
    