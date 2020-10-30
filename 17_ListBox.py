from tkinter import *

def print_selected():
    clicked_item = list1.curselection()
    print(clicked_item)


    for items in clicked_item:
        print(list1.get(items))


def del_selection():
    clicked_item = list1.curselection()
    for items in clicked_item:
        print(list1.delete(items))




root = Tk()

# By default width = 20 Height = 20
# Width: no of char in one line

root.geometry("400x400+200+200")

# list1 = Listbox(root, width=5, height=5,selectmode = BROWSE)   # BROWSE :- default mode
# list1 = Listbox(root, width=15, height=15,selectmode=SINGLE)
# list1 = Listbox(root, width=15, height=15,selectmode=MULTIPLE)
list1 = Listbox(root, width=15, height=15,selectmode=EXTENDED)

list1.pack()

list1.insert(1, 'Databse')
list1.insert(7, 'Oracle')
list1.insert(2, 'Python')
list1.insert(3, 'C++')
list1.insert(4, 'Java')
list1.insert(5, 'Ruby')
list1.insert(6, '.Net')


btn = Button(root, text='print',command= print_selected).pack()

btn_del = Button(root, text='delete', command=del_selection).pack()


root.mainloop()