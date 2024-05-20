import random 
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
pc_cards = []
def deal_card(lista):
    lista.append(random.choice(cards))

def first_deal(lista1,lista2):
    deal_card(lista1)
    deal_card(lista1)
    deal_card(lista2)
    deal_card(lista2)


first_deal(user_cards, pc_cards)


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you 
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

user_score = sum(user_cards)
pc_score = sum(pc_cards)

print(user_score)