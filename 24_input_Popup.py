#simpledialog


from tkinter import *
from tkinter import simpledialog
root = Tk()

def get_details():
    string = simpledialog.askstring('Ask question', 'Enter your name')
    integer = simpledialog.askinteger('Ask question', 'Enter you age')
    float_no = simpledialog.askfloat('Ask question', 'Enter your sal')
    float_no = float_no/5

    print(string + ' ' + str(integer) + ' ' + str(float_no))
    # print(integer)
    # print(float_no)

    name = Label(root,text='Name').pack()
    age = Label(root, text='Age').pack()
    sal = Label(root, text='sal').pack()

    entry_name = Entry(root,text= name)
    entry_name.pack(side=LEFT)

btn = Button(root,text='ask question', command= get_details).pack(side=TOP)

root.mainloop()