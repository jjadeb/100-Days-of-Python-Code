from turtle import Turtle, Screen
import random

# Set up screens
race_screen = Screen()
text_screen = Screen()

# Initiate turtles
red = Turtle()
blue = Turtle()
purple = Turtle()
yellow = Turtle()
pink = Turtle()

# Create turtle list
turtles = [red, blue, purple, yellow, pink]
finishers = []

# Set turtle attributes
red.color("red")
blue.color("blue")
purple.color("purple")
yellow.color("yellow")
pink.color("pink")

color_list = ""
for turtle in turtles:
    turtle.penup()
    turtle.shapesize(3)
    turtle.shape("turtle")
    color_list += f"{turtle.fillcolor()}; "


# Get user race bet
bet = text_screen.textinput("Betting Choice",
                            f"Choose a turtle to bet on: {color_list} \n Then press space to start.")

# Get turtles to initial spots
height = race_screen.window_height()
width = race_screen.window_width()


def places_please():
    """Put turtles in their starting spots"""
    w = -4*(width/10)
    h = -2*(height/6)

    for t in turtles:
        t.setx(w)
        t.sety(h)
        h += height/6


def race():
    """Turtles race across the screen"""
    places_please()
    while len(finishers) != len(turtles):
        for t in turtles:
            advance = random.randint(0, 10)
            t.forward(advance)
        finishing_turtles()
    race_screen.bye()
    winner = finishers[0]
    print(f"The winning turtle is {winner}.")
    check_bet()


def check_bet():
    """Check if the users bet matches the winning turtle and print result"""
    if bet == finishers[0]:
        print("You win gold!")
    elif bet == finishers[1]:
        print(f"{str.title(bet)}'s place is {check_turtle_placement()}nd. You win silver!")
    elif bet == finishers[2]:
        print(f"{str.title(bet)}'s place is {check_turtle_placement()}rd. You win bronze!")
    else:
        print(f"You lose. {str.title(bet)}'s place is {check_turtle_placement()}th.")


def check_turtle_placement():
    return finishers.index(bet) + 1


def finishing_turtles():
    """Check if turtles cross finish line, if so add them to finishers"""
    for t in turtles:
        if t.xcor() >= width:
            color = t.fillcolor()
            if not finishers.__contains__(color):
                finishers.append(color)


# Other screen attributes
race_screen.listen()
race_screen.onkey(key="space", fun=race)
race_screen.exitonclick()



