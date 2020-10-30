from tkinter import *
from tkinter import filedialog

def open_file():
    res = filedialog.askopenfile(mode='r',title= 'Open a file', initialdir = 'C://Users//sanjay.kumar12//Desktop//KT_20',
                                 filetypes=(("text fiels",'*.txt'),('All files','*.*')))
    for i in res:
        print(i)


def save_file():
    fs = filedialog.asksaveasfile(mode='w',title= 'Save your file', defaultextension=".txt", initialdir = 'C://Users//sanjay.kumar12//Desktop//KT_20')
    fs.write('hello world')
    fs.close()

root = Tk()

btn1 = Button(root,text='Open File',command=open_file)
btn1.pack()


btn2 = Button(root,text='Save As', command=save_file)
btn2.pack()


# cannot use pack() with parameter if using in below ways.
Button(root,text='Close',command=root.quit).pack()

root.geometry('300x300+150+150')
root.mainloop()

