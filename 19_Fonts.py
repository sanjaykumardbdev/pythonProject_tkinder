from tkinter import *
from tkinter.font import Font
from tkinter import font
root = Tk()

# my_font = Font(family="Helvetica", size=16)
# must be -family, -size, -weight, -slant, -underline, or -overstrike

#my_font = Font(family="Times New Roman", size=16, weight = 'bold', slant='italic', underline = 1)
my_font = Font(family="Times New Roman", size=16, weight = 'bold', slant='roman', underline=1, overstrike=1)

label = Label(root, text='Hello World',font=my_font).pack()


root.geometry('400x400+400+300')


fonts = list(font.families())
for i in fonts:
    print(i)



root.mainloop()