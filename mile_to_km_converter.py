from tkinter import *

def miles_to_km():
	miles = float(miles_input.get())
	km = miles * 1.609
	miles_to_km_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#Input (miles_input)
miles_input=Entry(width=7)
miles_input.grid(column=1, row=0)

#is equal to Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#Miles Label (miles_label)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#Km Label 
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Miles to Km Value Label (kilometer_result_label)
miles_to_km_label = Label(text="0")
miles_to_km_label.grid(column=1, row=1)

#Button
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop() 