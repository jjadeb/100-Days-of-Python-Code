from replit import clear

bids = {}
cont = True

while cont:
  name = input("What is your name: ")
  bid = int(input("What is your bid: $"))
  bids[name] = bid
  more = input("Are there other users who want to bid? Type yes or no: ")
  if more == "no":
    cont = False
  else:
    clear()

highest_bid = 0
highest_name = "no one"
for name in bids:
  if bids[name] > highest_bid:
    highest_bid = bids[name]
    highest_name = name

print(f"The winner is {highest_name} with a bid of ${highest_bid}.")
  