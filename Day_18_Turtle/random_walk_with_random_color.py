import turtle as t
import random
tor = t.Turtle()
t.colormode(255)

tor.pensize(15)
tor.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

for i in range(200):
    tor.color(random_color())
    steps = 30
    angle = random.choice([0,90,180,270])
    tor.fd(steps) 
    tor.setheading(angle)

