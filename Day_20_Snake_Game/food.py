from turtle import Turtle
import random


class Food(Turtle):
    """Food for the snake to eat"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.random_location()

    def random_location(self):
        """Moves food to a random location"""
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)