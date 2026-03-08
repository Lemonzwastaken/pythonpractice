import os
import random
from art import *

def normal_auction():
    """The main bidding game"""

    bidders_dict = {}
    #BIDDING
    bidding_status = True
    while bidding_status:
        print(logo)
        print(f"Current Bidders:\n{bidders_dict}")
        name = input("What is your name: \n").title()

        try:
            bid_amt = int(input("What is your bidding amt(in $):\n$"))
            bidders_dict[name] = bid_amt
            print(bid_registered)
        except ValueError:
            print("❌ Invalid input. Please enter a whole number (e.g., 100).")

        if (input("Do you wanna add another participant('Enter to continue, EXIT to exit'): \n")).lower() == "exit":
            bidding_status = False
        else:
            os.system('cls' if os.name=='nt' else 'clear')

    #CHECKING
    max_bid = 0
    max_bidder = None
    for bidder in bidders_dict:
        if bidders_dict[bidder] > max_bid:
            max_bid = bidders_dict[bidder]
            max_bidder = bidder
        else:
            pass
    
    print(f"The highest bidder is: {max_bidder}\nWith a bid of ${max_bid}")

def silent_auction():
    """Silent Auction Game"""

    bidders_dict = {}
    #BIDDING
    bidding_status = True
    while bidding_status:
        print(logo)
        name = input("What is your name: \n").title()

        try:
            bid_amt = int(input("What is your bidding amt(in $):\n$"))
            bidders_dict[name] = bid_amt
            print(bid_registered)
        except ValueError:
            print("❌ Invalid input. Please enter a whole number (e.g., 100).")

        if (input("Do you wanna add another participant('Enter to continue, EXIT to exit'): \n")).lower() == "exit":
            bidding_status = False
        else:
            os.system('cls' if os.name=='nt' else 'clear')

    #CHECKING
    max_bid = 0
    max_bidder = None
    for bidder in bidders_dict:
        if bidders_dict[bidder] > max_bid:
            max_bid = bidders_dict[bidder]
            max_bidder = bidder
        else:
            pass
    
    print(f"The highest bidder is: {max_bidder}\nWith a bid of ${max_bid}")

def random_auction():
    bidders_list = []

    bidding_status = True

    while bidding_status:
        print(logo)
        print(f"Current bidders: {bidders_list}")
        name = input("What is your name: \n").title()
        bidders_list.append(name)
    
        if (input("Do you wanna add another participant('Enter to continue, EXIT to exit'): \n")).lower() == "exit":
                bidding_status = False
        else:
            os.system('cls' if os.name=='nt' else 'clear')

    winner = random.choice(bidders_list).upper()

    print(f"THE WINNER FOR TODAYS RANDOM BID IS: {winner}")