import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

#CONTROLS:
screen.listen()

screen.onkeypress(fun=player.move_front, key="Up")
screen.onkeypress(fun=player.move_front, key="w")

screen.onkeypress(fun=player.move_back, key="s")
screen.onkeypress(fun=player.move_back, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.06)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    

    #When player crosses the finish line
    if player.ycor() >= player.FINISH_LINE_Y:
        player.goto(player.STARTING_POSITION)
        scoreboard.LEVEL += 1
        scoreboard.update_scoreboard()
        car_manager.RANDOM_CHANCE -=1
    
    #Player win
    if car_manager.RANDOM_CHANCE <=1:
        scoreboard.win()
        game_is_on = False
    
    #Player Collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.loose()
            game_is_on = False



screen.exitonclick()
    
