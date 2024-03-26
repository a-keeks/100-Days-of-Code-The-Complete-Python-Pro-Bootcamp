# Blind Auction

import os
from art import logo
print(logo)

print("Welcome to the Silent Auction program")

def clear():
    os.system('cls')

bids = {}

add_another_bidder = True
while add_another_bidder:
    name = input("What is your name?\n")
    bid_amount = input("Enter your bid amount:\n£")
    bids[name] = bid_amount
    again = input('Are there any other bidders? Type "yes" or "no"\n')
    if again == "yes":
        clear()
    elif again == "no":
        clear()
        add_another_bidder = False
        highest_bid = max(bids.values())
        highest_bidder = max(bids, key = bids.get)

        print(f"The winner is {highest_bidder} with a bid of £{highest_bid}")
