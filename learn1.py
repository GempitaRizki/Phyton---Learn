from ast import Delete
from cProfile import label
from tkinter import *
root =  Tk ()

root.geometry("500x300")
root.title("Gempita Rizki Ramadhan")
root.iconbitmap("icon.ico")

e = Entry (root,show = "*")
e.grid ()

def submit ():
    lbl = Label(root,text = e.get())
    lbl.grid()

def detele():
    e.delete(0,None)


btn = Button(root,text = "submit", command=submit)
btn.grid()
btn2 = Button(root,text = "delete", command=Delete)
btn2.grid()




root.mainloop()