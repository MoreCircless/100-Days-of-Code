from data import data
from art import logo, vs
import random
import os




def format_text(option):
    name = option["name"]
    description = option["description"]
    country = option["country"]
    return f"{name}, is a {description} from {country}"


def comparator(guess, optiona, optionb):
    if guess == "a":
        if optiona['follower_count'] > optionb['follower_count']:
            return True
        else:
            return False
    else:
        if optiona['follower_count'] > optionb['follower_count']:
            return False
        else:
            return True 

    




option_b = random.choice(data)



points = 0


is_on = True

while is_on:
    option_a = option_b
    option_b = random.choice(data)
    print(logo)
    print(f"Score: {points}")
    print(f"Option A: {format_text(option_a)}")  
    print(vs)
    print(f"Option B: {format_text(option_b)}")  
    
    print("Who has more followers, option 'A' or option 'B'")
    guess = input("-> ").lower()
    bool_guess = comparator(guess, option_a, option_b)
    os.system('clear')
    if bool_guess:
        print("Correct!")
        points += 1
    else:
        print("Wrong :(")
        is_on = False

print(f"Your final score is: {points}")

