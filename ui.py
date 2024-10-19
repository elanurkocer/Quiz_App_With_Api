from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(bg="white" ,width=300,height=250)
        
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.text = self.canvas.create_text(150,
                                             125,
                                             text="lol",
                                             width=200,
                                             fill=THEME_COLOR,
                                             font=("Ariel",15,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2)
        
        self.label = Label(text="Score:",fg="white",bg=THEME_COLOR)
        self.label.grid(column=1,row=0,pady=10)
        
        self.button_t = Button(image=self.true_image,command=self.true_pressed)
        self.button_t.config(bg=THEME_COLOR,highlightthickness=0)
        self.button_t.grid(column=0,row=2,pady=20)
        
        self.button_f = Button(image=self.false_image,command=self.false_pressed)
        self.button_f.config(bg=THEME_COLOR,highlightthickness=0)
        self.button_f.grid(column=1,row=2,pady=20)
        
        self.get_new_q()
        
        self.window.mainloop()

    def get_new_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="The end")
            self.button_t.config(state="disabled")
            self.button_f.config(state="disabled")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_new_q)