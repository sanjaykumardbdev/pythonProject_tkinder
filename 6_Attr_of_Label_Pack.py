# Attribute:
# how to use label and pack attribute to get GUI:

# import Tkinter
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()


from tkinter import *
root = Tk()

# widthxhegith+x-asix+y-axis

root.geometry("444x233+400+250")
root.minsize(344, 333)
root.maxsize(944, 933)

root.title("San Window")

# Imp label option

# text = adds the text
# bd = backgroud
# fg = foregroud
# font sets the font
# padx = x padding      horizontal, to get extra width
# pady = y padding      vertical, to get extra height
# relief = portder styling = SUNKEN, raised, groove, ridge


# Label  The Label widget is used to provide a single-line caption for other widgets.
# It can also contain images.

title_label = Label(text = '''
    \nOpens a file for appending. The file pointer is at the end of the file 
    \nif the file exists. That is, the file is in the append mode.''',
                    bg = "green", fg = "black", padx = 1, pady = 1
                    )
title_label.pack()


# Button  The Button widget is used to display buttons in your application.

btn1 = Button(text = "click me")
btn1.pack()

canvas1 = Canvas()
canvas1.pack()


root.mainloop()
