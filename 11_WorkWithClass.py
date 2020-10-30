#Python GUI Tutorial - 8 - Working with classes

from tkinter import *

class myButtons:
    def __init__(self, master):
        self.printButton = Button(master, text="Print", command = self.printMessage)
        self.printButton.pack(side=LEFT)


        self.quitButton = Button(master, text="Quit", command=quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("message from constructor")


root = Tk()
myButtons(root)

root.mainloop()

