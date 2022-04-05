import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x220')
root.resizable(False, False)
root.title('Multi Choice Quiz')


class Quiz:
    def __init__(self, parent):
        self.v = tk.StringVar(value="")
        self.v.set = (0)

        selected_answer = self.v.get()
        ans = (('14', 'Incorrect, sorry!'),
         ('7', 'Incorrect, try again!'),
         ('5', 'Incorrect, try again?'),
         ('4', 'Correct answer! Well done!'),
         ('53', 'Incorrect, very incorrect'))




q = Quiz(root)
root.mainloop()