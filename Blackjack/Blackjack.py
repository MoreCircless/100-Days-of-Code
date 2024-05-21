import random
import os


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
pc_cards = []

user_hand = 0
pc_hand = 0

is_on = True

def pc_deal():
    while pc_hand < 16:
        pc_cards.append(deal_card())
        hands_sum()
        hands_comprobation()


def hands_sum():
    global user_hand
    global pc_hand
    user_hand = sum(user_cards)
    pc_hand = sum(pc_cards)


def firs_deal():
    """This function append 2 cards to the card of the users"""
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    pc_cards.append(deal_card())
    pc_cards.append(deal_card())


def deal_card():
    """When this function gets called returns a random card that is in the CARDS list"""
    return random.choice(CARDS)


def hands_comprobation():
    global is_on
    if pc_hand == 21:
        print("PC has a BlackJack\nComputer WINS!")
        is_on = False
    elif user_hand == 21:
        print("You have a Blackjack\nYou WIN!!")
        is_on = False
    elif user_hand > 21:
        if 11 in user_cards:
            user_cards[user_cards.index(11)] = 1
        elif user_hand > 21:
            print("You over score 21, you lose :(")
            is_on = False
    elif pc_hand > 21:
        if 11 in user_cards:
            user_cards[user_cards.index(11)] = 1
        elif pc_hand > 21:
            print("PC score goes over 21, you WIN!!")
            is_on = False


firs_deal()

print(f"You hand is a {user_cards[0]}, {user_cards[1]}")
print(f"Computer visible card is a {pc_cards[0]}\n")

while is_on:
   
    hands_sum()
    hands_comprobation()
    print("Want another card?")
    print(f"Your hand -> {user_hand}")
    another_card = input("(Y)es or (N)o -> ").lower()
    if another_card == "y":
        new_card = deal_card()
        user_cards.append(new_card)
        print(f"The new card is {new_card}")
        hands_sum()
        print(f"Your hand -> {user_hand}")
        hands_comprobation()

    print(f"Hand value -> {user_hand}")
    hands_comprobation()   
    print(f"Computer visible card is a {pc_cards[0]}\n")
    pc_deal()
    





