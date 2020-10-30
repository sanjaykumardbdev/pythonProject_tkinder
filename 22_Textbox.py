from tkinter import *

root = Tk()

frame = Frame(root)

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)


txtbox = Text(frame,yscrollcommand=scroll.set)
txtbox.pack(side=LEFT)
scroll.config(command=txtbox.yview)

for i in range(100):
    txtbox.insert(END, 'List no: ' + str(i))


Button(root, text='quit', command=root.quit).pack(side=BOTTOM)
frame.pack()



root.geometry("300x400+400+150")
root.mainloop()
