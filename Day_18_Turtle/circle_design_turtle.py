import turtle as t
import random



tor = t.Turtle()
t.colormode(255)
tor.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r,g,b)
    return color

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tor.color(random_color())
        tor.circle(100)
        tor.setheading(tor.heading() + gap_size)


draw_spirograph(2)

scr = t.Screen()
scr.exitonclick()

