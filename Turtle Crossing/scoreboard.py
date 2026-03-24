from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        #constants
        self.FONT = ("Courier", 24, "normal")
        self.LEVEL = 1
        self.POS = (-200,250)

        self.goto(self.POS)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.LEVEL}", align="center", font=self.FONT)

    def win(self):
        self.clear()
        self.goto(0,0)
        self.write(f"YOU WIN", align="center", font=self.FONT)

    def loose(self):
        self.clear()
        self.goto(0,0)
        self.write(f"YOU DIED :(", align="center", font=self.FONT)
