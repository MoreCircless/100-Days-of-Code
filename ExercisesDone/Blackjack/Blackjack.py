import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      `------'                           |__/           

      """


def deal_card() -> int:
    """When this function gets called return a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def computer_play():
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        deal_card(computer_cards)


def winner_checker(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose "
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def clear():
    os.system("clear")


def first_deal():
    """This function generate the first deal adding two cards to the players hand"""
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(lista) -> int:
    """When this function gets called returns the total of the sum of the terms in the player hand"""
    suma = sum(lista)
    if suma == 21 and len(lista) == 2:
        return 0
    if 11 in lista and suma > 21:
        lista.remove(11)
        lista.append(1)
    return suma

def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    
    game_state = True
    
    first_deal()
    while game_state:
        
        user_score  = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards[0]} and {user_cards[1]}, score {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_state = False
    else:
        user_deal = input("Do you want another card?\n(Y)es or (N)o").lower()
        if user_deal == "y":
            user_cards.append(deal_card())
        else:
            game_state = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score)) 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()







    





