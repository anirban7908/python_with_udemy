# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
bid_data = {}
no_bidder_remain = False

while not no_bidder_remain:
    bidder_name = input("Enter Your Name: ")
    bid = input("Enter Your Bid: ")

    bidder_check = input("Are there any other bidder? (Yes/No): ").lower()
    if bidder_check == "no":
        no_bidder_remain = True
    bid_data[bidder_name] = bid
    print("\n"*20)

max_bidder = max(bid_data, key=bid_data.get)
max_bid = bid_data[max_bidder]
print(f"The Winner is {max_bidder} with a bidding price of ${max_bid}")



