from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        #CONSTANTS
        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280
        
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.goto(self.STARTING_POSITION)
        self.setheading(90)

    
    def move_front(self):
        self.forward(self.MOVE_DISTANCE)

    def move_back(self):
        self.backward(self.MOVE_DISTANCE)