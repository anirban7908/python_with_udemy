from turtle import Turtle, Screen
import random
tor = Turtle()
tor_color = ['Blue','Turquoise', 'LimeGreen', 'Red', 'DarkSalmon', 'DarkViolet']
tor.pensize(15)
tor.speed("fastest")
for i in range(200):
    # steps = int(random() * 10)
    tor.color(random.choice(tor_color))
    steps = 30
    angle = random.choice([0,90,180,270])
    tor.fd(steps) 
    tor.setheading(angle)

scr = Screen()
scr.exitonclick()