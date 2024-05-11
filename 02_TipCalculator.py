#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇


print("Hola bienvenido a Tipper! \nAplicacion para el control de propinas")

cuenta = float(input("Precio de la cuenta?\n-> "))
propina = float(input("Que porcentaje de propina quieres dejar?\n-> "))
personas = int(input("Entre cuantas personas quiere dividir la cuenta?\n-> "))

precio_por_persona = (cuenta + (cuenta * (propina/100))) / personas

print(f"El precio por persona sera de {precio_por_persona:.2f} $")

print("Gracias por usar Tipper!!!")