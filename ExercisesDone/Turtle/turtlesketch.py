from turtle import *



tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(5)


def move_backward():
    tim.backward(5)
    
def move_left():
    tim.left(5)
    
def move_right():
    tim.right(5)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()
    
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()

