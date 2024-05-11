import random

print("Welcome to ROCK, PAPER, SCISSORS!!!")
print("What do you choose???")

player = input("(R)ock, (P)aper or (S)cissors?\n-> ")
computer_choice = None
computer = random.randint(0,2)
if computer == 0:
    computer_choice = "R"
elif computer == 1:
    computer_choice = "P"
elif computer == 2:
    computer_choice = "S"

def rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def scissors():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def player_chose():
    print("Player chose:")
def computer_chose():
    print("Computer chose:")

if player.capitalize == "R" and computer == "R":
    player_chose()
    rock()
    computer_chose()
    rock()
'''
    if player.capitalize == "R" and computer == "P":
        player_chose()
        rock()
        computer_chose()
        paper()
    if player.capitalize == "R" and computer == "S":
        
    if player.capitalize == "P" and computer == "R":
        print("YOU WINS!")
    if player.capitalize == "P" and computer == "P":
        print("TIE")
    if player.capitalize == "P" and computer == "S":
        print("COMPUTER WINS")
    if player.capitalize == "S" and computer == "R":
        print("Computer wins")
    if player.capitalize == "S" and computer == "P":
        print("You wins")
    if player.capitalize == "S" and computer == "S":
        print("TIE")
'''


print("GAME FINISHED!!")