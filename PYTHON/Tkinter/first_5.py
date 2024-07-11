from tkinter import *
def getvalue():
    #  a=uservalue.get()
    #  b=passvalue.get()
     print(uservalue.get())
     print(passvalue.get())
    
    
root=Tk()
root.geometry("655x333")

user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid(row=0)
password.grid(row=1)

#vsriable classes in tkinter
#BooleanVar,DoubleVar,IntVar,StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvalue).grid()
root.mainloop()