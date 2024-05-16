#Calculator

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


num1 = input("What is the first number?\n-> ")
num2 = input("What is the second number?\n-> ")
