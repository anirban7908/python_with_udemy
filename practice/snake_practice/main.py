from turtle import Screen, Turtle
import time
from snake import Snake




# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game practice")
screen.tracer(0)

#snake class
snake = Snake()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.3)
    # for segment in segments:
    #     segment.fd(20)
    snake.move_snake()

























screen.exitonclick()