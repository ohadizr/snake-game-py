from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def game_over():
    scoreboard.game_over()
    global game_is_on
    game_is_on = False


def restart_game():
    global game_is_on
    snake.reset()
    scoreboard.reset()
    game_is_on = True


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(restart_game, "space")

game_is_on = True

while True:
    screen.update()
    if game_is_on:
        time.sleep(0.1)
        snake.move()

        # collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
                snake.head.ycor() > 290 or snake.head.ycor() < -290):
            game_over()

        # collision with tail
        for segment in snake.segments:
            if segment != snake.head and snake.head.distance(segment) < 10:
                game_over()

screen.onkey(screen.bye, "Escape")
screen.mainloop()
