import random

def welcome():
    logo = """
    ______ _     _ _______ _______ _______      _______ _     _ _______      __   _ _     _ _______ ______  _______  ______     
    |  ____ |     | |______ |______ |______         |    |_____| |______      | \  | |     | |  |  | |_____] |______ |_____/     
    |_____| |_____| |______ ______| ______|         |    |     | |______      |  \_| |_____| |  |  | |_____] |______ |    \_     
                                                                                                                            

    """
    print(logo)
    print("Welcome to the GUESS THE NUMBER game!!!")
    print("In order to win you need to guess the name")
    print("There are two levels of difficulty, easy and hard")
    print("Easy -> 10 Attempt")
    print("Hard -> 5 Attempt")
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


welcome()

number_to_guess = int(random.randint(1,100))



game_diff = input("What difficult you wan't the game to be?\nType 'easy' or 'hard'\n-> ")

if game_diff == "easy":
    trys = 10
elif game_diff == "hard":
      trys = 5

print(number_to_guess)
status = True 

while status == True:
    user_try = int(input("Guess the number\n-> "))
    if user_try > number_to_guess:
        print("Too high")
        trys -= 1
    elif user_try < number_to_guess:
        print("Too low")
        trys -= 1
    elif user_try == number_to_guess:
        print("YOU WIN!!")
        status = False
    if trys == 0:
        print("You lose :(")
        status = False 
        
    if status == True:
        print(f"You have {trys} lives left")
    




