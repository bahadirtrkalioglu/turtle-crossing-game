import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.walk)

timer = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    #Arabaya çarpıp çarpmadığını anlamak
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Bitiş çizgisine geldi mi?
    if player.is_at_finish_line():
        player.go_home()
        car_manager.level_up()
        scoreboard.increase_level()

    car_manager.create_car()
    car_manager.move_cars()


screen.exitonclick()
