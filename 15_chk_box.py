from tkinter import *


def click_me():
    print(i.get())


def close_app():
    root.quit()


def click_me_again():
    print(j.get())


root = Tk()

i = IntVar()
c = Checkbutton(root,text='Click Me', variable = i)
c.pack()

btn = Button(root,text="Find",command = click_me)
btn.pack()


# check for by default : directly click on button without action on
j = StringVar()
c1 = Checkbutton(root,text='Click Me text',variable=j, offvalue = 'Unchecked', onvalue = 'Checked')
c1.pack()


btn1 = Button(root,text='Click Me Again',command = click_me_again)
btn1.pack()



btn_close = Button(root,text= 'Close', command = close_app, bg = 'blue', fg = 'white')
btn_close.pack()

root.mainloop()