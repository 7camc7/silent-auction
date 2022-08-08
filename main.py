import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

bids = {}
another_bidder = True

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while another_bidder:
  enter_name = input("What is your name? ")
  enter_price = int(input("What is your highest bid? $"))
  bids[enter_name] = enter_price
  another_bidder = input("Is there another bidder:yes or no? ")
  cls()
  if another_bidder == "no":
    another_bidder = False
    highest_bidder(bids)
    

