from tkinter import *


root = Tk()

root.geometry('400x600')

canvas = Canvas(root, width=200, height=200, bg='blue')
canvas.pack()

#xy- widthHeight
#line1 = canvas.create_line(0,0,200,100, fill = 'yellow')
#line2 = canvas.create_line(200,100,0,200, fill = 'red')

canvas.create_arc(100,200,200,200, fill = 'yellow')

root.mainloop()
