from tkinter import  *


def new_win():
    top_win = Toplevel()
    top_win.geometry('300x300+150+150')
    top_win.title('Top Window')
    btn1 = Button(top_win,text='Close top win', command=top_win.destroy)
    btn1.pack(side=LEFT)




root = Tk()

btn1 = Button(root,text='New Window',command=new_win)
btn1.pack()


root.geometry('300x300+150+150')
root.mainloop()