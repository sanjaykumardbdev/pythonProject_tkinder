from tkinter import *

root = Tk()


name = Label(root,text = "Username")
password = Label(root, text = "Password")

entry1 = Entry(root)
entry2 = Entry(root)
# entry3 = Entry(root)
# entry4 = Entry(root)

#column is default to 0:
name.grid(row=0, sticky=E)
entry1.grid(row=0, column=1)

password.grid(row=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text = "Keep me logged in", width=0, height=0,onvalue = 1, offvalue = 0)
c.grid(columnspan=2)

# sub_btn = Button(root, text= 'OK')
# entry3.grid(row = 3, column = 3)
#
# can_btn = Button(root, text= 'Cancel')
# entry4.grid(row = 3, column = 4)






root.mainloop()