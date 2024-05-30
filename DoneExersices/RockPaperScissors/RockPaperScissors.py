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

def player_chose(name):
    print(f"Player chose:{name}")
def computer_chose(name):
    print(f"Computer chose:{name}")

def player_win():
    print("Player Win!!!")
def computer_win():
    print("Computer Win!!!")
def tie():
    print("It is a tie!!!")


if player == "P":
    player_chose("Paper")
    paper()
    if computer_choice == "P":
        computer_chose("Paper")
        paper()
        tie()
    elif computer_choice == "R":
        computer_chose("Rock")
        rock()
        player_win()
    elif computer_choice == "S":
        computer_chose("Scissors")
        scissors()
        computer_win()
elif player == "R":
    player_chose("Rock")
    rock()
    if computer_choice == "P":
        computer_chose("Paper")
        paper()
        computer_win()
    elif computer_choice == "R":
        computer_chose("Rock")
        rock()
        tie()
    elif computer_choice == "S":
        computer_chose("Scissors")
        scissors()
        player_win()
elif player == "S":
    player_chose("Scissors")
    scissors()
    if computer_choice == "P":
        computer_chose("Paper")
        paper()
        player_win()
    elif computer_choice == "R":
        computer_chose("Rock")
        rock()
        computer_win()
    elif computer_choice == "S":
        computer_chose("Scissors")
        scissors()
        tie()
else:
    print("Invalid input!!!")


print("GAME FINISHED!!")