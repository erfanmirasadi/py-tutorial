from turtle import Screen, Turtle
from snack import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snack game")
screen.tracer() #animation 

snack = Snake()

game_is_on = True

while game_is_on:
    screen.update() #update the animation (sceen tracer)
    time.sleep(0.2)

    snack.move()
    
screen.exitonclick()
