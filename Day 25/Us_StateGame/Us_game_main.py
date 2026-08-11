import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. State Game")
score=0
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state=[]
state_data=pandas.read_csv("50_states.csv")

while len(guessed_state)<50:
    answer = screen.textinput(f"{score}/50", "Enter another state")
    data_row = state_data[state_data["state"] == answer.title()]
    if data_row is not None:
        guessed_state.append(data_row.state.item())
        score+=1
        t=turtle.Turtle()
        t.penup()
        t.goto(data_row.x.item(),data_row.y.item())
        t.write(data_row.state.item())
    else:
        continue

screen.exitonclick()
