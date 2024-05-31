from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
middle = Scoreboard()
middle.middle()
scoreboard.update_scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while True:
    screen.update()
    ball.move()
    time.sleep(ball.sleep)
    
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()
    
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()
    
    if ball.xcor() > 450:
        ball.restart()
        ball.bounce()
        scoreboard.l_point()
        
    if ball.xcor() < -450:
        ball.restart()
        ball.bounce()
        scoreboard.r_point() 



