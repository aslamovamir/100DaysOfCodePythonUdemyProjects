from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# creating the right and left paddle objects
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)

# making the screen listen for the keys
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

# creating the ball
ball = Ball()


# the game is kept running until the boolean is True
game_on = True
while game_on:
    time.sleep(ball.speed_move)
    screen.update()
    ball.default_move()

    # detecting collision of ball with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision of ball with the paddle
    # the speed of the ball also increases
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detecting if the ball passes the right wall, meaning the left paddle scores
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.passed_paddle()
    # detecting if the ball passes the left wall, meaning the right paddle scores
    elif ball.xcor() < -390:
        scoreboard.r_point()
        ball.passed_paddle()

screen.exitonclick()
