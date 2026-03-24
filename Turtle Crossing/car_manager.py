from turtle import Turtle
import random



class CarManager:
    def __init__(self):

        #CONSTANTS
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.RANDOM_CHANCE = 20
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,self.RANDOM_CHANCE)
        if random_chance == 1 or random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(self.COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.MOVE_INCREMENT)