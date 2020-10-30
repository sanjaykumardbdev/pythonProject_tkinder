# important pkg to call
from tkinter import *

#create object of call tkinter
top = Tk()
# Code to add widgets will go here...

# Width x Height
top.geometry("999x444")

top.minsize(200, 100)
top.maxsize(733, 433)

label1 = Label(text= "Hello this is my first program")
label1.pack()

top.mainloop()
