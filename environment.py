from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import numpy as np


class SnakeEnvironment:
    def __init__(self):
        # Set up the screen
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game trained by ML")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

    def reset(self):
        self.snake.reset()
        self.scoreboard.reset()
        return self.get_state()

    def step(self, action):
        # Translate the action to a direction
        if action == 0:
            self.snake.up()
        elif action == 1:
            self.snake.down()
        elif action == 2:
            self.snake.left()
        elif action == 3:
            self.snake.right()
        elif action == 4:  # Continue in the current direction
            pass

        self.snake.move()

        # Define your reward system and detect if the game has ended (done)
        reward = -0.5  # Reward for each step
        done = False

        # Check collision with food
        if self.snake.head.distance(self.food) < 20:
            self.food.refresh()
            self.scoreboard.increase_score()
            self.snake.extend()
            reward = 10

        # Check collision with wall or tail
        if (self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or
                self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280):
            done = True
            reward = -100

        for segment in self.snake.segments:
            if segment != self.snake.head and self.snake.head.distance(segment) < 10:
                done = True
                reward = -100

        return self.get_state(), reward, done

    def render(self):
        # Update the visual representation
        self.screen.update()

    def close(self):
        self.screen.bye()

    def get_state(self):
        x_diff = self.food.x - self.snake.head.xcor()
        y_diff = self.food.y - self.snake.head.ycor()
        direction_to_food = (np.sign(x_diff), np.sign(y_diff))

        # Adding more state information: distances to walls
        distance_to_top_wall = 300 - self.snake.head.ycor()
        distance_to_bottom_wall = self.snake.head.ycor() + 300
        distance_to_right_wall = 300 - self.snake.head.xcor()
        distance_to_left_wall = self.snake.head.xcor() + 300

        # Normalizing the distances to lie between 0 and 1
        distance_to_top_wall /= 300
        distance_to_bottom_wall /= 300
        distance_to_right_wall /= 300
        distance_to_left_wall /= 300

        return direction_to_food, (distance_to_top_wall, distance_to_bottom_wall, distance_to_right_wall, distance_to_left_wall)
