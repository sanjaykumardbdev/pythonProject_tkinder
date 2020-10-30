# Python GUI Tutorial - 9 - creating drop down menus

from tkinter import *
root = Tk()


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


#1: create instance of Menu class
main_menu = Menu(root)


#============================================================
# File Menu
#============================================================
file_menu_child = Menu(main_menu, tearoff=0)
file_menu_child.add_command(label="New",command=donothing)
file_menu_child.add_command(label="Save",command=donothing)
main_menu.add_separator()
file_menu_child.add_command(label="Save As",command=donothing)

#2: configure main_menu to horizontal bar
root.config(menu=main_menu)
#3: write name of menu bar and associate child menu to named menu;
main_menu.add_cascade(label="File",menu=file_menu_child)


#============================================================
# Edit Menu
#============================================================
edit_menu_child = Menu(main_menu, tearoff=0)
edit_menu_child.add_command(label="Cut",command=donothing)
edit_menu_child.add_command(label="Copy",command=donothing)
edit_menu_child.add_separator()
edit_menu_child.add_command(label="Paste",command=donothing)

root.config(menu=main_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu_child)


#============================================================
# Help Menu
#============================================================





root.mainloop()
