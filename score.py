from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.num_score = 0
        self.goto(0, 250)
        self.write(f"Score: 0", font=("Arial", 30, "normal"), align="center")

    def lvl_up(self):
        self.num_score += 1
        self.clear()
        self.write(f"Score: {self.num_score}", font=("Arial", 30, "normal"), align="center")

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", font=("Verdana", 50, "normal"), align="center")
