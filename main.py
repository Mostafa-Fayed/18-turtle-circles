import turtle
from turtle import Turtle as T, Screen as S
import random

my_turtle = T()
my_turtle.shape("turtle")
my_turtle.pencolor("green")


my_turtle.speed(0)
my_turtle.width(1)
# color mode is changed from the module itself and not from the object.
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_circle(5)


my_screen = S()
my_screen.exitonclick()
