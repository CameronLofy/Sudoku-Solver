# python GUI

import tkinter
from tkinter import *

window = Tk()
window.title("Sudoku Solver")
lbl = Label(window, text="Sudoku", font=("Helvetica", 16, "bold italic"))
lbl.grid(column=0, row=0)
window.geometry('600x750')

refresh = Button(window, text="Refresh")
refresh.grid(column=0, row=1)


window.mainloop()