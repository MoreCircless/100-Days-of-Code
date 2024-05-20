import random
import os

game_state = True

def deal_card():
    """When this function gets called returns a random card"""
    return random.choice(cards)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def plus21():
    if user_hand > 21 or computer_hand > 21:
        return False 
    else:
        return True 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

usercards = [random.choice(cards), random.choice(cards)]

computercards = [random.choice(cards), random.choice(cards)]

print(usercards)
print(computercards)
usercards = [11, 11]
computer_hand = int(computercards[0]) + int(computercards[1])
user_hand = int(usercards[0]) + int(usercards[1])

if computer_hand == 21:
    print("Computer Wins!!")
    game_state = False 
elif user_hand == 21:
    print("User Wins!!")
    game_state = False 


print(f"Your hand has a value of {user_hand}")
print(f"Opponent first card is {computercards[0]}")

if user_hand > 21 and 11 in usercards:
    for card in usercards:
        if card == 11:
            usercards.index = 1


 
while game_state == True:
    game_state = plus21()

    user_choice = input("Do you want other card?\n(Y)es or (N)o ->")

    if user_choice == "Y":
        user_new_hand =[]
