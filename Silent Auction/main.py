from art import *
from functions import *

auction_running = True

while auction_running:
    print(logo)
    bidding()
    print(bid_registered)
    conti = input("Does anyone else wish to bid(Y/N): ").lower()
    if conti == "n":
        auction_running = False
    else:
        clear_screen()

highest_bidder()


