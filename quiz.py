from tkinter import *
import tkinter as tk

root = Tk()

class Application(tk.Frame):

    def __init__(self,title):
        tk.Frame.__init__(self)
        self.master.title(title)
        self.option_add('*Font','aerial 20 bold')
        self.pack(expand=tk.YES, fill=tk.BOTH)

        #widget for quiz app
        frame=iQuiz(self,column=1)
        frame.config(width=1000,height=500)
        frame.grid_propagate(0)
        que_label=label(frame,"question is here",row=1)
        opt1=radioButton(frame,"Option A is here",row=2)
        opt2=radioButton(frame,"Option B is here",row=3)
        opt3=radioButton(frame,"Option C is here",row=4)
        opt4=radioButton(frame,"Option D is here",row=5)
        ans_label=label(frame,"\nanswer will be shown on click of show me answer",row=6)
        answer=button(frame,"Show me answer",row=7)


        frame_pre=iQuiz(self,column=0)
        pre=button(frame_pre,'Previous')
        pre.config(bg='Powder blue',fg='white')

        frame_next=iQuiz(self,column=2)
        nxt=button(frame_next,'Next')
        nxt.config(bg='powder blue',fg='white')












if __name__=='__main__':
    Application('Quiz App').mainloop()
