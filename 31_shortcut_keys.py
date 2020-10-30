from tkinter import *
from tkinter import messagebox



def call_me(event=''):
    messagebox.showinfo("Infor","Hello World !!!!!!!")


root = Tk()


root.bind('<Control-d>', call_me)
btn1 = Button(root, text='Call Me ctrl+d', command=call_me)
btn1.pack()


root.geometry('300x300+150+150')
root.mainloop()
