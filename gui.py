# python GUI

import tkinter
from tkinter import *
font_temp = ("Helvetica", 16, "bold italic")
window = Tk()
window.title("Sudoku Solver")
lbl = Label(window, text="Sudoku", font=font_temp)
lbl.grid(column=0, row=0)
window.geometry('600x750')
def clicked():
    lbl2.configure(text=" Solution:")
solve = Button(window, text="Solve", bg="light blue", fg="black", font=font_temp, command=clicked)
solve.grid(column=0, row=1)

lbl2 = Label(window, text="Sudoku input:", font=font_temp)
lbl2.grid(column=1, row=1)


window.mainloop()