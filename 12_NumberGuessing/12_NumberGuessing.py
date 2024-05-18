import random
logo = """
  ______ _     _ _______ _______ _______      _______ _     _ _______      __   _ _     _ _______ ______  _______  ______     
 |  ____ |     | |______ |______ |______         |    |_____| |______      | \  | |     | |  |  | |_____] |______ |_____/     
 |_____| |_____| |______ ______| ______|         |    |     | |______      |  \_| |_____| |  |  | |_____] |______ |    \_     
                                                                                                                          

"""
print(logo)

print("Welcome to the GUESS THE NUMBER game!!!")
print("In order to win you need to guess the name")
print("There are two levels of difficulty, easy and hard")
print("Hard -> 5 Attempts)
print("Easy -> 10 Attempts")



number_to_guess = random.randint(1,100)



game_diff = input("What difficult you wan't the game to be?\nType 'easy' or 'hard')
