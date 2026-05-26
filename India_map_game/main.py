import turtle
import pandas

screen = turtle.Screen()

screen.title("Indian states Game")

image = "India_map.gif"

screen.addshape(image)
screen.setup(width=700,height=700)

turtle.shape(image)

state_data = pandas.read_csv("28_indian_states.csv")

state_list = state_data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    user_state = screen.textinput(title=f"{len(guessed_state)}/28 Correct", prompt="Enter the State name").title()

    if user_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in guessed_state:
                missing_state.append(state)
        new_state_data = pandas.DataFrame(missing_state)
        learn_state_csv = new_state_data.to_csv('learn_state.csv')
        break

    guessed_state.append(user_state)
    if user_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.speed(1)
        selected_state = state_data[state_data.state == user_state]
        t.goto(selected_state.x.item(), selected_state.y.item())
        t.write(selected_state.state.item())


