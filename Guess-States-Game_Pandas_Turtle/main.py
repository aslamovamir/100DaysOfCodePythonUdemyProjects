# import the library for turtle
import turtle
# import the pandas library
import pandas

# create a screen object
screen = turtle.Screen()
# get the path to and name of the image to load as a turtle shape
image = './blank_states_img.gif'
# create a new custom turtle shape with the image
screen.addshape(image)
# make the turtle object have that shape
turtle.shape(image)


# method to print the x and y coordinates of mouse click
def get_mouse_click_coor(x, y):
    print(x, y)


# user score and the list of guessed sates so far
USER_SCORE = 0
GUESSED_STATES = []

# create a pandas dataframe object
data = pandas.read_csv("./50_states.csv")

# create a list of guessed states
guessed_states = []

# lock the screen object so it does not close after mouse click
# turtle.mainloop()

# the user will keep guessing until all the 50 states are guessed
# we will loop 50 times
while len(guessed_states) <= 50:
    # get hold of the user input
    # title the input string for functionality purposes
    answer_state = screen.textinput(title=f'{USER_SCORE}/50 Correct States', prompt="What is another state's name?").title()

    # if the user types 'Exit' we want to break the loop (user input is titled)
    if answer_state == 'Exit':
        break

    # check if the user input corresponds to any data value in the SCV file
    if answer_state in data.values:
        # add the guessed state to the guessed_states list
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            # increase the user score
            USER_SCORE += 1

            # get hold of the coordinates of the state
            x_coordinate = data[data.state == answer_state].x.values[0]
            y_coordinate = data[data.state == answer_state].y.values[0]
            state_t = turtle.Turtle()
            state_t.penup()
            state_t.hideturtle()
            state_t.setposition(x_coordinate, y_coordinate)
            state_t.pendown()
            state_t.write(answer_state)


# after the termination of the game we will transfer 'missed states' as a CSV file

# # get all the states list from the CSV file
all_states = data.state.to_list()
print(all_states)

# loop through the all_states list and check if a state is in the guessed state list
# if it is not, put it in a new list
missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

print(missed_states)

# create a dataframe from scratch
missed_states_obj = {
    "Missed States": missed_states
}

# convert python object to pandas dataframe object
pandas_states_obj = pandas.DataFrame(missed_states_obj)

# save the dataframe object to a CSV file
pandas_states_obj.to_csv('./States_To_Learn.csv')
