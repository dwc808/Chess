import game
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Chess")

#overall frame
screen = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky =(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

