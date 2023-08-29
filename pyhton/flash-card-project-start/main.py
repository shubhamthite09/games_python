from tkinter import *
import pandas
import random
currant_card = {}
to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global currant_card,flip_timer
    window.after_cancel(flip_timer)
    currant_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=currant_card["French"], fill="black")
    canvas.itemconfig(card_background, image =card_front_img)
    flip_timer= window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=currant_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
def is_known():
    to_learn.remove(currant_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer= window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title",fill="black",font=("Arial", 40, "italic") )
card_word = canvas.create_text(400, 263, text="word",fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button1 = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=button1, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

button2 = PhotoImage(file="images/right.png")
known_button = Button(image=button2, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()








window.mainloop()