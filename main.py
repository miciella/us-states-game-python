import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

#add shape as image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")


all_states = states.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guess_states:
                missed_states.append(state)
        # convert list into dataframe
        not_guessed_states = pandas.DataFrame(missed_states)
        not_guessed_states.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # if answer_state == state in csv
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # gets the first element
        # state_data.state.item()
        t.write(answer_state)


screen.exitonclick()