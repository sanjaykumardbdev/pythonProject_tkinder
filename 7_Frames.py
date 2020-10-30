from tkinter import *

root = Tk()

root.geometry("400x400")

frame = Frame(root, width = 300, height=300)
btn1 = Button(frame, text = "Button_1")
btn2 = Button(frame, text = "Button_2")
btn1.pack(side = LEFT)
btn2.pack(side = LEFT)
frame.pack()


bottom_frm = Frame(root)
btn3 = Button(bottom_frm, text = "Button_3")
btn3.pack()
bottom_frm.pack()


bottomFrame = Frame(root)
btn4 = Button(bottomFrame, text = "down")
btn4.pack()
bottomFrame.pack()



one = Label(root,text = "One", bg = "red")
two = Label(root,text = "two", bg = "red")
three = Label(root, text = "three", bg = "blue")

one.pack()
two.pack(fill= X)
three.pack(side=LEFT, fill = Y)

root.mainloop()
