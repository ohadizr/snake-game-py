from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        # We use the refresh method to set the initial position.
        self.refresh()

    def refresh(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)
