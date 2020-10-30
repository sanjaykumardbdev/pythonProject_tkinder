from tkinter import *

root = Tk()

def click_me():
    #print(entry.get())
    if (entry.get() == 'sanjay'):
        print('success')
    else:
        print('Fail')

entry = Entry(root)
entry.pack()

btn = Button(root, text='click me', command=click_me).pack()


# ===========================


def click_me1():
    i1 = i.get()
    print(i1)
    #print(i.get())


i = StringVar()
entry1 = Entry(root,textvariable=i)
entry1.pack()

i.set("Welcome")
btn1 = Button(root, text='click here',command=click_me1)
btn1.pack()




root.geometry('400x300+400+300')

root.mainloop()