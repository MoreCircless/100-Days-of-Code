from os import read
from turtle import Screen, Turtle
import time
import random

# Screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

# Constants 
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# SnakeClass.py
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    
    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def extend(self):
        self.add_segments(self.segments[-1].position())
        
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
        
          
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
            
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
         
         
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
# Food.py

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()
    
    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
    
# Scoreboard
ALIGNAMENT = "Center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        with open("/home/manu/100-Days-of-Code/ExercisesDone/SnakeGameHS/data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        
            
        
        
                   
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} - High Score: {self.highscore}", move=False, align=ALIGNAMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/home/manu/100-Days-of-Code/ExercisesDone/SnakeGameHS/data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()    

                
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
          
# Code
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()


game_on = True



screen.exitonclick()

