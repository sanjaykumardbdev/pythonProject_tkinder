from tkinter import  *

def get_count():
    print(s.get())


root = Tk()


s = Spinbox(root,from_=1, to=10)
s.pack()


btn_cnt = Button(root,text='Get Value',command=get_count)
btn_cnt.pack()


btn1 = Button(root,text='close',command=root.quit)
btn1.pack()


root.geometry('300x300+150+150')
root.mainloop()

