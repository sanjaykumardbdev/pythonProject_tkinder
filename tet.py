from tkinter import *
root = Tk()

def click_me_str():
    print(j.get())


j = StringVar()

c1 = Checkbutton(root, text='male', value="radio 1", variable=j )
c2 = Checkbutton(root, text='female', value="radio 2", variable=j)
c1.pack()
c2.pack()



btn1 = Button(root, text='click again', command=click_me_str)
btn1.pack()




root.mainloop()