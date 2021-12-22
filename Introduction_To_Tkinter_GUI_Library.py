# import the library of the tkinter, a GUI library
import tkinter

# create a new window object from class Tk()
window = tkinter.Tk()

# change the title of the program
window.title("My first GUI Program")

# change the size of the window object
window.minsize(width=500, height=300)

# create a label from a Label class from the tkinter library
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# place the label onto the window with the "pack" method
# we can also specify where to pack the label with the parameter "side": options-bottom,left,right,top
# we can also make it "expand" onto the window
# my_label.pack(side="left")
my_label.pack()

# configure the properties of a component
# 1st way
my_label["text"] = "New Text"
# 2nd way
my_label.config(text="New Text")


# event listener for the button
def button_clicked():
    print("I got clicked")
    # also change the label text content
    # 1st way
    # my_label["text"] = "The button got clicked!"
    # 2nd way
    my_label.config(text=input.get())


# Button
# set the event listener to trigger the "button_clicked" function
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
# set the width of the entry component
input = tkinter.Entry(width=10)
# pack it onto the window
input.pack()
# get hold of the user input
print(input.get())
# when the button is clicked the text content of the label will change
# to the input of the user

# to keep the window object up on the screen, we need a loop
# we will use the method that comes with the tkinter library, "mainloop()"
window.mainloop()
