from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.setposition(0, 0)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.1

    def default_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.speed_move *= 0.9

    def passed_paddle(self):
        self.setposition(0, 0)
        self.speed_move = 0.1
        self.bounce_x()
