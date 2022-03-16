from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import json
import random
import time

LVL1 = 27
LVL2 = 53
LVL3 = 100

window = Screen()
window.colormode(255)
window.title("Snake")
window.setup(width=600, height=600)
window.bgcolor(153, 255, 153)
window.tracer(0)

game_mode = window.textinput("Game Mode", "Press 'y' for borders")

# create Snake
snake = Snake()
food = Food()
score = Score()
game_is_on = True
speed = 0.1

window.listen()

window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")


def score_name():
    name_input = window.textinput("Score", "Enter your name please.")
    new_data = {name_input: {"score: ": score.num_score}}

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=3)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=3)


while game_is_on:

    rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    time.sleep(speed)
    window.update()
    snake.move()
    snake.head.forward(20)

    if score.num_score < 5:
        if food.fillcolor() == (153, 255, 153):
            food.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if game_mode == "y":
        if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
            score_name()
            game_is_on = False
            score.game_over()
    else:
        if snake.head.xcor() > 290:
            snake.head.goto(-280, snake.head.ycor())
        if snake.head.xcor() < -290:
            snake.head.goto(280, snake.head.ycor())
        if snake.head.ycor() > 290:
            snake.head.goto(snake.head.xcor(), -280)
        if snake.head.ycor() < -290:
            snake.head.goto(snake.head.xcor(), 280)

    if snake.head.distance(food) < 18:
        snake.add_segment()
        food.refresh()
        if len(snake.segments) > LVL1:
            score.color("white")
        score.lvl_up()
        if speed > 0.005:
            speed -= 0.0005

    for _ in range(2, len(snake.segments)-1):
        if snake.head.distance(snake.segments[_]) < 3:
            score_name()
            game_is_on = False
            score.game_over()

    rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    if len(snake.segments) >= 100:
        window.bgcolor(rand_color)
        for n in snake.segments:
            n.color(rand_color)

    if LVL2 <= len(snake.segments) < LVL3:
        window.bgcolor("black")
        for n in snake.segments:
            n.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if LVL1 < len(snake.segments) < LVL2:
        window.bgcolor("black")
        if snake.head.fillcolor() == (200, 200, 0):
            for n in snake.segments:
                n.color(255, 255, 0)
        else:
            for n in snake.segments:
                n.color(200, 200, 0)

window.exitonclick()
