from tkinter import *

def miles_to_km():
    input = float(miles_input.get())
    calculated_val = round(input * 1.60934) 
    km_val.config(text=f"{calculated_val}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_val = Label(text="0")
km_val.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()