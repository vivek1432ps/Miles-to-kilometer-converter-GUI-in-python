import pandas
from tkinter import *

window = Tk()

window.title("My fist GUI program ")
window.minsize(width=600, height=300)

my_label = Label(text="I am program", font=("Arial", 24, "bold"))
my_label.pack()
# Label
my_label["text"] = "new Text"
my_label.config(text="New text")


# Button


def button_clicked():
    print("I am Clicked")
    new_text = input.get()
    a = my_label.config(text=new_text)



button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=10)
input.pack()
input.get()



window.mainloop()
