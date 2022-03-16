from turtle import Turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        for _ in INITIAL_POSITION:
            self.segment = Turtle("square")
            self.random_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.segment.color(self.random_color)
            self.segment.penup()
            self.segment.goto(_)
            self.segments.append(self.segment)
        self.head = self.segments[0]
        self.head.color("red")

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            last_segment = self.segments[n - 1]
            x_cor = last_segment.xcor()
            y_cor = last_segment.ycor()
            self.segments[n].goto(x_cor, y_cor)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_segment.goto(self.head.xcor(), self.head.ycor())
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

