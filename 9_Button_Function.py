from tkinter import *

root = Tk()

# 1st way to bind function with button
def call_me():
    print("You called me !")

btn1 = Button(root,text="Click Me",command=call_me)
btn1.pack()


# 2st way to bind function with button

def call_me_again(event):
    print("you called me again")

btn2 = Button(root,text="Again")
btn2.bind("<Button-1>", call_me_again)
btn2.pack()

# use only command to perfrom action:
def close_app():
    quitButton = Button(root,text="Close Me", command=root.quit())
    quitButton.bind("<Button-1>",)
    quitButton.pack()


root.mainloop()

