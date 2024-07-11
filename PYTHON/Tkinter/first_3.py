from tkinter import *
root=Tk()
root.geometry("655x333")
root.minsize(200,100)
f1=Frame(root,bg="skyblue",borderwidth=4,relief="sunken")
f1.pack(side="top",pady=20,padx=20)

f2=Frame(root,bg="lightpink",borderwidth=4,relief="sunken")
f2.pack(side="bottom",pady=20,padx=20) 

l1=Label(f1,text="tkinter i love you",fg="red")
l1.pack(pady=10,padx=10)

l2=Label(f2,text="Anchal i love you",fg="blue")
l2.pack(pady=10,padx=10)
root.mainloop()