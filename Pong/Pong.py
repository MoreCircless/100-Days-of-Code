from turtle import Turtle, Screen
import time


# Screen Setup
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)
screen.listen()

# Create and move Paddle 
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    
# Ball class

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
           
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
        
        
# Paddle class 
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def go_up(self):
        new_y = self.
        
# Scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    def l_point(self):
        
    
    



paddle = Turtle()

paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)

ball = Ball()

scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    time.sleep(ball.move_speed)
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        pass
    
    # Detect collision with paddles:
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
