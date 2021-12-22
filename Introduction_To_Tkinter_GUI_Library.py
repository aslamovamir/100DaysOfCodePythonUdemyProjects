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
my_label.pack(side="left")

# to keep the window object up on the screen, we need a loop
# we will use the method that comes with the tkinter library, "mainloop()"
window.mainloop()
