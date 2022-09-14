import random
import turtle as t
from turtle import Screen


color_list = [(224, 232, 240), (196, 165, 120), (148, 166, 183), (66, 104, 128), (223, 205, 124), (12, 35, 57), (185, 152, 165), (144, 88, 53), (147, 172, 158), (136, 75, 93), (185, 154, 44), (68, 110, 89), (13, 41, 31), (179, 95, 115), (76, 31, 19), (213, 178, 190), (183, 187, 209), (136, 30, 20), (20, 89, 62), (122, 33, 49), (66, 22, 33), (172, 205, 189), (34, 57, 108), (107, 124, 160), (18, 84, 98), (162, 204, 212), (72, 149, 167)]

tim = t.Turtle()
t.colormode(255)
t.color("forest green")
t.pensize(5)
t.speed("fastest")


def random_color():
    color = random.choice(color_list)
    return color


def draw(space, x):
    t.setheading(130)
    t.forward(500)
    t.setheading(0)
    for i in range(x):
        for j in range(x):
            t.dot(20, random.choice(color_list))

            t.forward(space)
        t.backward(space * x)

        # direction
        t.right(90)
        t.forward(space)
        t.left(90)


# Main Section
t.penup()
t.hideturtle()
draw(40, 16)

# hide the turtle



screen = t.Screen()
screen.exitonclick()