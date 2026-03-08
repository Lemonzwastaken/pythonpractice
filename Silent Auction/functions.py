import os
bidders_dict = {}

def bidding():
    """Begins the game of bidding, main engine"""

    name = input("What is your name: \n")
    bid_amt = int(input("What is your bidding amt(in $):\n$"))
    bidders_dict[name] = bid_amt

def highest_bidder():
    """This function decides the highest bidder"""

    max_bid = 0
    max_bidder = None
    for bidder in bidders_dict:
        if bidders_dict[bidder] > max_bid:
            max_bid = bidders_dict[bidder]
            max_bidder = bidder
        else:
            pass
    
    print(f"The highest bidder is: {max_bidder}\nWith a bid of ${max_bid}")

def clear_screen():
    """This function clears terminal. It doesn't work in PyCharm Run window"""
    
    os.system('cls')

