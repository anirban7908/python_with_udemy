from turtle import Turtle, Screen
import random

scr = Screen()
is_game_on = False
scr.setup(width=500, height=400)
user_bet = scr.textinput(title='Make your bet!', prompt="Which Turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
x_position = -230

all_turtle = []

for t_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle_colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x= x_position, y= y_position[t_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on = True


while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won the race. Winning turtle {winning_color}")
            else:
                print(f"You have lose the race. Winning turtle {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)



scr.exitonclick()