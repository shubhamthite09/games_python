from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR: str = "#375362"

class QuizeInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quzzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_lable = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_lable.grid(row=0,column=1)

        self.canvas = Canvas(width=400, height=350, bg="white")
        self.canvas_text = self.canvas.create_text(200,175,
                                                   width=380,
                                                   text="some text here",
                                                   fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.get_next_que()

        self.window.mainloop()

    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="you have attemted last question \n quiz end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_que)

