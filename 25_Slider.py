from tkinter import *
root = Tk()


frame1 = Frame(root)


s = Scale(frame1, width=20, length=50, from_=1, to=20)
s.pack(side=LEFT, fill=Y)


root.geometry('400x300+250+150')

frame1.pack(side = TOP)

root.mainloop()
