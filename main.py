from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Miki")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.sarpe1.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.sarpe1.xcor() > 280 or snake.sarpe1.xcor() < -280 or snake.sarpe1.ycor() > 280 or snake.sarpe1.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segmente[1:]:
        if snake.sarpe1.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
