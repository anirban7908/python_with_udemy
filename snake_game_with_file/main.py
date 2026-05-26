from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, MAX_RETRY
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

play_again = True

while play_again:
    snake.reset()
    scoreboard.reset()
    retry_count = 0
    sleep_time = 0.7
    is_game_on = True

    screen.listen()
    
    while is_game_on:
        snake.move()
        screen.update()
        time.sleep(sleep_time)

        current_score = scoreboard.score

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            if scoreboard.score % 2 == 0:
                sleep_time *= 0.9
        # Detect Collision with wall
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            retry_count += 1
            if retry_count > MAX_RETRY:  
                scoreboard.game_over()
            else:
                scoreboard.reset()
                snake.reset()
                scoreboard.game_over()
                sleep_time = 0.7

            is_game_on = False

        # Detect Collision with tail
        for segment in snake.segments[3:]:
            if snake.head.distance(segment) < 10:
                retry_count += 1
                if retry_count > MAX_RETRY:  
                    scoreboard.game_over()
                else:
                    scoreboard.reset()
                    snake.reset()
                    scoreboard.game_over()
                    sleep_time = 0.7
                
                is_game_on = False

    user_choice = screen.textinput(title="Game Over", prompt="Do you want to play again? Type 'yes' or 'no': ")

    if user_choice and user_choice.lower() == "yes":
        play_again = True
    else:
        play_again = False

screen.bye()

