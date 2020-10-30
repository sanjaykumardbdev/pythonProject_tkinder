# Python GUI Tutorial - 9 - creating drop down menus

from tkinter import *
root = Tk()


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


#1: create instance of Menu class
main_menu = Menu(root)
root.config(menu=main_menu)


fileMemu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File",menu=fileMemu)

editMemu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit",menu=editMemu)



#============================================================
# File Menu
#============================================================

fileMemu.add_command(label="New",command=donothing)
fileMemu.add_command(label="Save",command=donothing)
fileMemu.add_separator()
#fileMemu.add_command(label="Save As",command=donothing)
# creating sub menu

save_menu = Menu(fileMemu, tearoff=0)
fileMemu.add_cascade(label = 'Save As', menu = save_menu)

save_menu.add_command(label='save new',command=donothing)
save_menu.add_command(label='save now',command=donothing)


#
#
#
# #============================================================
# # Edit Menu
# #============================================================

editMemu.add_command(label="Cut",command=donothing)
editMemu.add_command(label="Copy",command=donothing)
editMemu.add_separator()
editMemu.add_command(label="Paste",command=donothing)
#
#
# #============================================================
# # Help Menu
# #============================================================
#




root.mainloop()
