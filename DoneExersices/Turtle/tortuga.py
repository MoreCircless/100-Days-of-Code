from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

turtle.speed("slow")



for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True
    
while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"{winner.capitalize()} WIN! YOU WIN! :)")
                game_on = False
            else:
                print(f"{winner.capitalize()} WIN! You lose :(")
                game_on = False
        steps_forward = random.randint(0,10)
        turtle.forward(steps_forward)



screen.exitonclick
