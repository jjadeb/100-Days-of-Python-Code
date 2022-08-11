from turtle import Turtle
from turtle import Screen
import math
import random

# Extracting colours from Hirst Artwork

# import colorgram
#
# colours = colorgram.extract("image.jpg", 25)
# rgb_colours = []
# for c in colours:
#     rgb_colours.append(c.rgb)
#
# rgb_colours = [tuple(rgb) for rgb in rgb_colours]
#
# print(rgb_colours)

# colour list without white

painting_colours = [(236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233), (239, 208, 94),
                    (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66),
                    (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161),
                    (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180)]

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed(0)
tim.up()
tim.hideturtle()

dist = 30
dot_size = 10
angle = 90

a = dist * 4.5
initial_travel = math.hypot(a, a)


def choose_colour():
    """Choose random colour from Hirst colour pallet"""
    colour = random.choice(painting_colours)
    return colour


def go_right():
    """Turtle makes a right u-turn"""
    tim.right(angle)
    tim.forward(dist)
    tim.right(angle)


def go_left():
    """Turtle makes a left u-turn"""
    tim.left(angle)
    tim.forward(dist)
    tim.left(angle)


def make_line():
    """Turtle makes a line of dots"""
    for i in range(9):
        tim.dot(dot_size, choose_colour())
        tim.forward(dist)
        tim.dot(dot_size, choose_colour())

def starting_point():
    """Centers drawing"""
    tim.seth(225)
    tim.forward(initial_travel)
    tim.seth(0)


def make_painting():
    """Turtle makes a filled square of dots"""
    starting_point()
    for i in range(5):
        make_line()
        go_left()
        make_line()
        go_right()


make_painting()

screen.exitonclick()
