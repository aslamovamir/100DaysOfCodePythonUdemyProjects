import turtle
from turtle import Turtle, Screen
import random


def make_square(turtle_o):
    for i in range(4):
        turtle_o.forward(100)
        turtle_o.right(90)


def walk_dashed(num_steps):
    for _ in range(num_steps):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_the_shapes(turtle_o):
    shape_indexes = [3, 4, 5, 6, 8, 9, 10]
    num_steps = 100
    pen_colors = ["aquamarine", "bisque", "cyan", "DarkGreen", "DeepSkyBlue",
                  "DarkSlateGray", "chocolate", "gold"]
    total_deg = 360

    for shape in shape_indexes:
        angle = total_deg // shape
        turtle_o.pencolor(pen_colors[random.randint(0, len(pen_colors) - 1)])

        # num of straight walks determined the number of sides of the shape
        for stride in range(shape):
            turtle_o.right(angle)
            turtle_o.forward(num_steps)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk(turtle_o):
    # basically the decisive factor of random motion is the angle by which the object turns
    # afterwards, the object just moves forward by the fixed amount of distance
    # we assume the object only moves "forward", not "backward"
    # let's create a list of reasonable angles
    angles = [0, 90, 180, 270]  # no need for a 360 degree turn as 0 degree is functionally equivalent
    fixed_stride = 30

    # we let the object to randomly decide how many strides it will make
    rand_strides = random.randint(1, 500)  # not from 0, but from 1, to account for the range function
    print(f"The turtle decided to do {rand_strides} strides!")
    turtle_o.pensize(10)
    turtle_o.speed("fast")
    for stride in range(0, rand_strides):
        # we let the object to randomly choose any color from the list above
        turtle_o.pencolor(random_color())

        # we let the object to randomly choose to turn either right or left
        rand_turn = random.randint(0, 2)
        if rand_turn:  # if it is 1, the object decides to turn right
            turtle_o.right(angles[random.randint(0, len(angles) - 1)])
        else:  # if it is 0, the object decides to turn left
            turtle_o.left(angles[random.randint(0, len(angles) - 1)])
        turtle_o.forward(fixed_stride)


def draw_spirograph(turtle_o, gap_size):
    turtle_o.speed("fastest")
    for _ in range(int(360 / gap_size)):
        turtle_o.color(random_color())
        turtle_o.circle(100)
        turtle_o.setheading(turtle.heading() + gap_size)


# Main
tim = Turtle()
tim.shape("turtle")
tim.color("coral3")
turtle.colormode(255)
draw_spirograph(tim, 3)

screen = Screen()
screen.exitonclick()
