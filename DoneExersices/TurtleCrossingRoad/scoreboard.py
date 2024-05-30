from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.write_lvl()        
        
        
    def next_level(self):
        self.level += 1  
        self.write_lvl()
        
    def write_lvl(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=FONT)

        
