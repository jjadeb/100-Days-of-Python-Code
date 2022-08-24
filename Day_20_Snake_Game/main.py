from turtle import Screen
import time
from snake import Snake
from score_board import ScoreBoard
from food import Food
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food.xcor(), food.ycor()) < 15:
        food.random_location()
        score_board.update_score()
        snake.add_segment()

    # Detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_board.game_over()

    # Detect tail collision
    if snake.tail_collide():
        game_is_on = False
        score_board.game_over()

screen.exitonclick()

