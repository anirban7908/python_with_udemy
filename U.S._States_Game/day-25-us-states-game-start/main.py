import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# Get the coordinates of the screen point on mouse click.
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# alternative of screen.exitonclick()
# turtle.mainloop()



# screen.exitonclick()

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
