

print("Welcome to Treasure Island!!!\nYour mission is to find the treasure")


print("step 1")
movement1 = input("What you do? (L)eft or (R)ight?")

if movement1 != "l" or movement1 != "L":
    print("You fall into a hole noooo...\nGAME OVER")
elif movement1 == "l" or movement1 == "L":
    print("step 2")
    movement2 = input("What do you choose? (S)wim or (W)ait?")
    if movement2 != "W" or movement2 != "w":
        print("OH NO!!, you have being attacked by trouts\nGAME OVER")
    if  movement2 == "W" or movement2 == "w":
        print("step 3")
        movement3 = input("Which door do you choose? (R)ed, (Y)ellow or (B)lue?")
        if movement3 == "R" or movement3 == "r":
            print("YOU HAVE BEEN BURNED!!!\nGAME OVER")
        elif movement3 == "Y" or movement3 == "y":
            print("YOU WIN!!!")
        elif movement3 == "B" or movement3 == "b":
            print("YOU ARE BEING EATEN BY BEAST!!\nGAME OVER")
        else:
            print("Game over")

print("Game finished!")