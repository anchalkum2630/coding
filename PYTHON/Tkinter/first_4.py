from tkinter import *
root=Tk()
root.geometry("655x333")

def hello():
    print("hello world")

def when():
    print("hello India")

def how():
    print("hello Jharkhand")

def what():
    print("hello Parent")

frame=Frame(root,borderwidth=3,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="blue",text="print",command=hello)
b1.pack(side="left",padx=10)

b2=Button(frame,fg="blue",text="print",command=when)
b2.pack(side="left",padx=10)

b3=Button(frame,fg="blue",text="print",command=how)
b3.pack(side="left",padx=10)

b4=Button(frame,fg="blue",text="print",command=what)
b4.pack(side="left",padx=10)

root.mainloop()