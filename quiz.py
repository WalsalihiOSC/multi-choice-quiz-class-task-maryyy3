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

        #label
        label = ttk.Label(text="How many stars are on the New Zealand flag?")
        label.pack(fill='x', padx=5, pady=5)

        # radio buttons
        for ans in ans:
            r = ttk.Radiobutton(parent,text=ans[0],value=ans[1],variable=self.v.get())
            r.pack(fill='x', padx=5, pady=5)

         # button
        button = ttk.Button(parent, text="Submit answer", command=self.selected_answer)
        button.pack(fill='x', padx=5, pady=5)

    def selected_answer(self):
        showinfo(title='answer', message=self.v.get())


q = Quiz(root)
root.mainloop()