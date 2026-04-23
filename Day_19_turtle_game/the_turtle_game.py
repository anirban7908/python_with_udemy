from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()

def move_forwards():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def move_anti_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
scr.listen()
scr.onkey(key="w", fun=move_forwards)
scr.onkey(key="s", fun=move_backward)
scr.onkey(key="a", fun=move_anti_clockwise)
scr.onkey(key="d", fun=move_clockwise)
scr.exitonclick()