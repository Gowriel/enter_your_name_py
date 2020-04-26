from tkinter import *

root = Tk()

e = Entry(root, width=30, borderwidth=3)
e.pack()

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()