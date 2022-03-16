from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.color(rand_color)


