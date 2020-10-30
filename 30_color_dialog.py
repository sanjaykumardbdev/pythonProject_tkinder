from tkinter import  *
from tkinter import colorchooser


def find_color():
    x = colorchooser.askcolor('red',title='Choose your color')
    print(x)
    print(x[0])
    print(x[1])

    root.configure(background=x[1])

root = Tk()



btn1 = Button(root,text='New Window',command=find_color)
btn1.pack()


root.geometry('300x300+150+150')
root.mainloop()