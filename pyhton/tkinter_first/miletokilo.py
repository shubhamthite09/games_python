from tkinter import *
def miles_to_km():
    miles = float(miles_input.get())
    km = miles  * 1.609
    kilometer_result.config(text=f"{km}")

window = Tk()
window.title("Miles to kilogram converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)
miles_lable = Label(text = "Miles")
miles_lable.grid(column=2,row=0)
is_equle_lable = Label(text ="is equal to")
is_equle_lable.grid(column=0,row=1)
kilometer_result = Label(text="0")
kilometer_result.grid(column=1,row=1)
kilometer_lable = Label(text="Km")
kilometer_lable.grid(column=2,row=1)
calcute_button = Button(text = "Calculate", command=miles_to_km)
calcute_button.grid(column=1,row=2)
window.mainloop()
