import tkinter

window = tkinter.Tk()
window.title("my frist gdi program")
window.minsize(width=500, height=300)

my_lable = tkinter.Label(text="new text", font=("Arial" , 24, "bold"))
my_lable.grid(row=0,column=0)
def button_click():
    my_lable.config(text=input.get())
button = tkinter.Button(text="click me", command=button_click)
button.grid(row=1, column=2)
button1 = tkinter.Button(text="new button")
button1.grid(row=0, column=3)
input = tkinter.Entry()
input.grid(row=4, column=4)







window.mainloop()