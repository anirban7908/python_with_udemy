from turtle import Turtle, Screen
import random

tor = Turtle()
tor.pu()
tor.sety(tor.ycor() + 200)
tor.pd()

tor_color = ['Blue','Turquoise', 'LimeGreen', 'Red', 'DarkSalmon', 'DarkViolet']
min_lines = 3

max_lines = 10


def draw_shape(num_of_lines):
    angle = 360
    for _ in range(0, num_of_lines):
        tor.fd(100)
        current_angle = angle / num_of_lines
        tor.right(current_angle)


for __ in range(min_lines, max_lines):
    tor.color(random.choice(tor_color))
    draw_shape(__)


scr = Screen()

scr.exitonclick()
