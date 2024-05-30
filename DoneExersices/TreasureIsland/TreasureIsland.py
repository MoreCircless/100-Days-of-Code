

print("Welcome to Treasure Island!!!\nYour mission is to find the treasure")

def treasure():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
importado = treasure()   
gameover = 0
print('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')

step1 = input("Do you go (L)eft or (R)ight?\n-> ")
if step1 == "L":
    print("You\'ve come to a lake. There is an island in the middle of the lake.")
    step2 = input("(S)wim or (W)ait?\n-> ")
    if step2 == "W":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        step3 = input("Which door? (R)ed, (Y)ellow or (B)lue\n-> ")
        if step3 == "R":
            print("Burned by fire!!!")
        elif step3 == "Y":
            treasure()
            print("YOU WIN!!!")
            gameover += 1
        elif step3 == "B":
            print("You are being eaten by beasts!!")
    else:
        print("You are being attacked by trout!!")
else:
    print("You fall into a hole!!!")

if gameover == 0:
    print("GAME OVER")

