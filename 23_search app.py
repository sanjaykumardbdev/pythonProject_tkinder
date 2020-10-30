from tkinter import *
import wikipedia


def get_me():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT,'Please check you input or internet connection')
    print(answer_value)


root = Tk()


topframe = Frame(root)

entry = Entry(topframe)
entry.pack()


button = Button(topframe, text='Search', command=get_me)
button.pack()


topframe.pack(side=TOP)

bottomframe = Frame(root)


scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

answer = Text(bottomframe, width=30, height=10, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()


bottomframe.pack(side=BOTTOM)




Button(bottomframe, text='quit', command=root.quit).pack(side=BOTTOM)





root.mainloop()