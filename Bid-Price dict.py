bids = {}
bidding_finished = False

while not bidding_finished:
    # 1. Ask for name and bid price
    name = input("What is your name?: ")
    price = int(input("What is your bid price?: $"))

    # 2. Add name and bid into the dictionary
    bids[name] = price

    # 3. Ask if there is a new bidder
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True

# 4. Declare the winner
highest_bid = 0
winner = ""

for person in bids:
    bid_amount = bids[person]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = person

print(f"The winner is {winner} with a bid of ${highest_bid}!")