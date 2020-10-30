from tkinter import *


root = Tk()

lframe = LabelFrame(root,text='Secton-1', padx=10, pady=10)
lframe.pack()

entry = Entry(lframe)
entry.pack()

Button(lframe, text='Close it', command=root.quit).pack()


root.geometry('300x300+150+150')
root.mainloop()

