import pandas as pd
import turtle
IMAGE = "/home/manu/100-Days-of-Code/PandasCSV/USquiz/day-25-us-states-game-start/blank_states_img.gif"
PATH = "/home/manu/100-Days-of-Code/PandasCSV/USquiz/day-25-us-states-game-start/50_states.csv"
is_on = True
total_guess = 0
guessed_states = []
# Screen SETUP

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Panda SETUP
data = pd.read_csv(PATH)


# Turtle SETUP
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()



answer_state = screen.textinput(title="Guess a State", prompt="What is your guess?")

while is_on:
    for state in data.state:
        if answer_state.capitalize() == state and answer_state.capitalize() not in guessed_states:
            guessed_states.append(state)
            total_guess += 1
            row = data[data.state == state]
            state_x = row['x'].values[0]
            state_y = row["y"].values[0]
            turtle.goto(state_x, state_y)
            turtle.write(state, align= "center")
            
            
    answer_state = screen.textinput(title=f"Guess a State - {total_guess}|50", prompt="What is next guess?")
    if total_guess == 50:
        is_on = False
    
    

screen.exitonclick()