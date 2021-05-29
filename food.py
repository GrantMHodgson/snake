from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        # food for snake is placed in random location
        self.move_food()

    def move_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

