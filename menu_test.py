from tkinter import *
root = Tk()

def do_nothing():
    print("nothing")

menubar = Menu(root)
root.config(menu=menubar)


file_menu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File',menu=file_menu)


edit_Menu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label ='Edit', menu=edit_Menu)


file_menu.add_cascade(label ="New",command = do_nothing)
file_menu.add_cascade(label="Open", command = do_nothing)

save_menu = Menu(file_menu, tearoff = 0)
save_menu.add_command(label='save as',command = do_nothing)
save_menu.add_command(label='save now',command = do_nothing)

file_menu.add_cascade(label='Save As',menu=save_menu)




root.mainloop()
