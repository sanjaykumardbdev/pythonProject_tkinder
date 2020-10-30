from tkinter import *

root = Tk()

def rightClick(event):
    print("Right clicked")

def leftClick(event):
    print("Right clicked")

def middleClick(event):
    print("Right clicked")

frame = Frame(root,width = 300, height = 300)

frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", rightClick)
frame.bind("<Button-3>", middleClick)
frame.pack()


root.mainloop()