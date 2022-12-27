import art as lg

# Function for clear
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to add to Dictionary
auction_bids = []


def add_dict(name, price):
    bids = {}
    bids['name'] = name
    bids['bid'] = price
    auction_bids.append(bids)


auction = True
while auction == True:

    """Import Logo"""
    print(lg.logo)

    # Questions to ask user
    name = input("The name of the person bidding: ")
    price = int(input("What is your bid: £"))
    user = input("Does another person wish to make bid(Y/N): ").lower()

    # Add user input into dictionary
    add_dict(name, price)

    # Check if another person wishes to make bid
    if user == 'no' or user == 'n':
        break
    else:
        clear()
        continue

max_value = None
for highest_bid in auction_bids:
    if max_value is None or highest_bid['bid'] > max_value:
        max_value = highest_bid['bid']
        max_bid = highest_bid['name']

print(f"The highest bid was £{max_value}, and the winner of this Auction: {max_bid}!")


