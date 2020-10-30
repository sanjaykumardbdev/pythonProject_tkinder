from tkinter import *
from tkinter.ttk import Combobox

root = Tk()


def print_select():
    print(c.get())


root.geometry("300x300+400+300")

v = ['c', 'c++', 'java', 'python', 'oracle']
# v = list(range(1, 5))



# default height min = 3 max = 10, width= default 10 : no. of char in horizontal


c = Combobox(root, values=v, height=1)
c.pack()
c.set("select")


btn = Button(root, text = 'click', command= print_select).pack()

root.mainloop()
