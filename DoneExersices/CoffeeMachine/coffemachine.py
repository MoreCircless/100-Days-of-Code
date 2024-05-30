
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


logo = """
   ( (
    ) )
  ........
  |      |]
  \      /    
   `----'
"""

money = 0

def ing_check(ing) -> bool:
   res_needed = MENU[ing]
   ret = True 
   ingre = res_needed["ingredients"]
   if resources["water"] < ingre["water"]:
      ret = False
   if resources["milk"] < ingre["milk"]:
      ret = False 
   if resources["coffee"] < ingre["coffee"]:
      ret = False 
   return ret 

def no_resources():
   print("There is no resources enough!\n Sorry")

def payment(choice):
   global money
   quarters = input("Quarters -> ")
   dimes = input("Dimes -> ")
   nickles = input("Nickles -> ")
   pennies = input("Pennies -> ")
   coffe_choice = MENU[choice]
   total_payment = 0.25 * float(quarters) + 0.10 * float(dimes) + 0.05 * float(nickles) + 0.01 * float(pennies)
   print(f"Your payment: {total_payment: .2f}$")
   if float(coffe_choice["cost"]) >= total_payment:
      print("Not enough money!\nReturning money...")
      return False     
   else:
      print("Enough money!")
      money += coffe_choice["cost"]
      return_money = total_payment - coffe_choice["cost"]
      print(f"Your return {return_money: .2f}$")
      return True 

   
def product_update(selection):
   choice_coffee = MENU[selection]
   ingredients = choice_coffee["ingredients"]
   resources["coffee"] -= ingredients["coffee"]
   resources["water"] -= ingredients["water"]
   resources["milk"] -= ingredients["milk"]
   


   


def report():
   print(f"\nWater -> {resources['water']}ml\nMilk -> {resources['milk']}ml\nCoffee -> {resources['coffee']}gr\nMoney -> {money}$")

print(logo)
print("Welcome to the coffe machine!")

while True:
   print("What would you like? (espresso/latte/cappuccino)")

   user_choice = input("-> ")
   if user_choice == "espresso":
      if ing_check("espresso"):
         print(f"The cost of {user_choice} is {MENU['espresso']['cost']}$")
         payment_check = payment("espresso")
         if payment_check:
            product_update("espresso")
      else:
         no_resources()
   elif user_choice == "latte":
      if ing_check("latte"):
         print(f"The cost of {user_choice} is {MENU['latte']['cost']}$")
         payment_check = payment("latte")
         if payment_check:
            product_update("latte")
      else:
         no_resources()
   elif user_choice == "cappuccino":
      if ing_check("cappuccino"):
         print(f"The cost of {user_choice} is {MENU['cappuccino']['cost']}$")
         payment_check = payment("cappuccino")
         if payment_check:
            product_update("espresso")
      else: 
         no_resources()
   elif user_choice == "off":
      break
   elif user_choice == "report":
      report()
   else:
      print("error!, not valid input")

