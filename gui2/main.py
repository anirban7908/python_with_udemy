from tkinter import *

def button_clicked():
    # my_label["text"] = input.get()
    my_label.config(text=input.get())

window=Tk()
window.title("My first GUI programme")
# configure window dimentions
window.minsize(width=500, height=300)
# Add paddign to all window elements from all four sides
window.config(padx=20, pady=20)

# Label
my_label = Label(text="My Label", font=("arial", 24, "bold"))
# pack() = The pack() method is one of Tkinter's three geometry managers used to arrange widgets within a window. It is the simplest to use, primarily stacking widgets vertically or horizontally relative to each other.
# my_label.pack()
my_label.grid(column=0, row=0)
# add pading to a single element
my_label.config(padx=10, pady=10)


# button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="I am New", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
user_data = input.get()
# input.pack()
input.grid(column=3, row=2)


window.mainloop()