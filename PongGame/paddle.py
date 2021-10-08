import turtle
from turtle import Turtle

UP = 90
DOWN = 270


# The paddle will inherit from the Turtle class and have inherited methods
class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        # the shape of the paddle is a square
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
