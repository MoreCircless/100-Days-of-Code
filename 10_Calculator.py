#Calculator
print("""
     
 _____________________
|  _________________  |
| | Calculator   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| 
      """)

#Add
def add(n1,n2):
    return n1 + n2

#Sustract
def sus(n1, n2):
    return n1 - n2

#Multiply
def mult(n1, n2):
    return n1 * n2

#Divide 
def div(n1,n2):
    return n1 // n2

operations = {
    "+": add,
    "-": sus,
    "*": mult,
    "/": div
}
still = True
while still == True:
    num1 = int(input("What is the first number?\n-> "))
    num2 = int(input("What is the second number?\n-> "))
    print("What operation you wan't to do?")
    for op in operations:
        print(op)
    operation_choice = input("-> ")

    to_do = operations[operation_choice]

    result = to_do(num1, num2)

    print(f"Result of {num1} {operation_choice} {num2} is {result}")

    print("You wan't to do more operations?")
    follow = str(input("(Y)es or (N)o\n-> " ))

    if follow == "Y":
        still = True 
    else:
        still = False 


print("Thanks for using this calculator!!")

