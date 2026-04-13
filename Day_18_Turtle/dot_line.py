from turtle import Turtle, Screen

tor = Turtle()

for _ in range(0, 10):
    tor.pd()
    tor.fd(10)
    tor.pu()
    tor.fd(10)

screen = Screen()
screen.exitonclick()
