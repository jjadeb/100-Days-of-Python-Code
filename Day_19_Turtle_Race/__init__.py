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
    while winning_turtle() == "":
        for t in turtles:
            advance = random.randint(0, 10)
            t.forward(advance)
    race_screen.bye()
    winner = winning_turtle()
    print(f"The winning turtle is {winner}.")
    check_bet(winner)


def check_bet(winner):
    """Check if the users bet matches the winning turtle and print result"""
    if bet == winner:
        print("You win!")
    else:
        print(f"You lose! You chose {bet}.")


def winning_turtle():
    """Check if there is a winning turtle, if so return color"""
    for t in turtles:
        if t.xcor() >= width:
            return t.fillcolor()
    return ""


# Other screen attributes
race_screen.listen()
race_screen.onkey(key="space", fun=race)
race_screen.exitonclick()



