from tkinter import *
root = Tk()

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------


def click_me():

    if i.get() == 1:
        print('Male')
    else:
        print('Female')


i = IntVar()
r1 = Radiobutton(root, text='Male',variable=i, value = 1)
r2 = Radiobutton(root, text='Fename',variable=i , value = 2)
r1.pack()
r2.pack()


btn = Button(root,text='you are', command = click_me)
btn.pack()

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


def click_me_str():
    print(j.get())


j = StringVar()

c1 = Radiobutton(root, text='Male', value="male", variable=j )
c2 = Radiobutton(root, text='Female', value="female", variable=j)
c1.pack()
c2.pack()



btn1 = Button(root, text='click again', command=click_me_str)
btn1.pack()



root.mainloop()