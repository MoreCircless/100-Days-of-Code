# Secret Auction Program
import os
bid_dict = {}
print("""        
      /(  ___________
     |  >:===========`
      )(
""")
print("Welcome to the Secret Auction Program!")
auction = True 
while auction == True:

    name = input("What is your Name?\n-> ")
    bid = input("What is your bid\n-> $ ")

    bid_dict[name] = bid

    more = str(input("More users?\n(Y)es or (N)o\n->"))
    if more == "Y":
        auction = True
    else:
        auction = False
    os.system("cls")

higher_bid = 0
winner = None

for key in bid_dict:
    bid_value = int(bid_dict[key])
    if bid_value > higher_bid:
        winner = key
        higher_bid = bid_value


print(f"The winner is {winner}, with {higher_bid} $")
    




