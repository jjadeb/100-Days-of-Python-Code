from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    """Displays score at the top of the screen"""

    def __init__(self):
        super().__init__()
        self.score = -1
        self.pencolor("white")
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Add one to score and update GUI"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'Game Over' sign"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
