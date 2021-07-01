from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to kilometer Converter")
window.minsize(width=200, height=100)

miles_input = Entry(width=20)
miles_input.focus()
miles_input.grid(column=1, row=0, padx=10, pady=10)

label = Label(text="Miles")
label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to ")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text=" 0 ")
kilometer_result_label.grid(column=1, row=1)

kilometer_KM_label = Label(text=" KM ")
kilometer_KM_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()
