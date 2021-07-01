from tkinter import *
from tkcalendar import *

# Window
screen = Tk()
screen.title("Test Layout")
screen.minsize(width=600, height=400)

# Label

label = Label(text="Test label")

label.config(text="Test Label", font=("Arial", 24))
label.pack()


# Buttons create


# Buttons function
def button_function():
    print("hello word")
    return "hello"


# Button
button = Button(text="OK", command=button_function)
button.pack()

# Entry

entry = Entry(width=30)
# Add same text
entry.insert(END, string="Enter your email here")
print(entry.get())
entry.pack()

# Text Box

text = Text(width=30, height=5)
# focus() it's used to puts cursor in textbox
text.focus()
text.insert(END, "Exame of multi-line text entry")
print(text.get("1.0", END))
text.pack()


# Spinbox

def sinpbox_used():
    # get the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=sinpbox_used)
spinbox.pack()


# Scale

# called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckBox
def chceckbox_used():
    # prints 1 if on button checked Otherwise 0,

    print(checked_state.get())


# variable to hold on to checked state,0 is off, 1 is on.

checked_state = IntVar()
checkbutton = Checkbutton(text="is on?", variable=checked_state, command=chceckbox_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar
# radio_button 1
radiobutton1 = Radiobutton(text="option1 Eg:male", value=1, variable=radio_state, command=radio_used)
# radio_button 2
radiobutton2 = Radiobutton(text="option2 Eg:female", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()


# Listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(heigh=4)
fruits = ["apple", "pear", "orange", "banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Add Calender


Label(screen, text='Date of Birth', font=("Arial", 24)).pack(padx=10, pady=10)

calendar_ = DateEntry(screen, width=30, bg="durable", fg="white", year=2020, )

calendar_.pack()

screen.mainloop()
