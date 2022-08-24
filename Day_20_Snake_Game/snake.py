from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def design_turtle(t):
    t.shape("square")
    t.fillcolor("white")
    t.penup()


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates snake on screen"""
        position = 0
        for t in range(0, 3):
            t = Turtle()
            design_turtle(t)
            t.goto((position * -20, 0))
            position += 1
            self.segments.append(t)

    def move(self):
        """Moves snake forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_place = self.segments[seg_num - 1]
            x = new_place.xcor()
            y = new_place.ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        """Adds segment to snake"""
        t = Turtle()
        design_turtle(t)
        position = self.segments[-1].pos()
        t.setpos(position)
        self.segments.append(t)

    def tail_collide(self):
        for i in self.segments[1:]:
            if i.distance(self.head.pos()) < 15:
                return True
        return False

    def up(self):
        """Turns snake upwards, if not facing downwards"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns snake downwards, if not facing upwards"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns snake to the left, if not facing right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns snake right, if not facing left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
