from tkinter import *
from tkinter import messagebox

root = Tk()

def approve():
    messagebox.showinfo("Approved","Approval done")

def warning():
    messagebox.showwarning("Warning","Not Valid")

def error():
    messagebox.showerror("Error", "Need to check err")

def closeApp():
    answer = messagebox.askquestion('Close', 'Do you really want to close')
    print(answer)
    if answer == 'yes':
        root.quit()

def yes_no_cancel():
    answer = messagebox.askyesnocancel('Exit','Do you really want to close')
    if answer:
        root.quit()
    else:
        pass




approve_btn = Button(root, text="OK", command = approve)
approve_btn.pack()

warning_btn = Button(root, text="Warning", command = warning)
warning_btn.pack()

err_btn = Button(root,text='show err', command = error)
err_btn.pack()

exit_btn = Button(root,text = 'Close', command = closeApp)
exit_btn.pack()

exit_btn1 = Button(root,text = "Close", command = yes_no_cancel)
exit_btn1.pack()



root.mainloop()
