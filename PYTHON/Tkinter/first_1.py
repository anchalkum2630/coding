# import tkinter
# print("imported")
from tkinter import *
from PIL import ImageTk,Image
root = Tk()  # make object of tkinter to use....write all the code between tk and mainloop

root.geometry("600x600")
root.minsize(200,200) #to give minsize
root.maxsize(900,900) #to give maxsize

#to write some thing in page
page=Label(text="Anchal Page")
page.pack()

#to attach photos

# image=Image.open('pic_3.jpg')
photo=PhotoImage(file="screen_1.png")
# photo=ImageTk.PhotoImage(Image.open('pic_3.jpg')) #both way can be used
photo_img=Label(image=photo)
photo_img.pack()


root.mainloop()
# other than tkinter what are the other ways to create gui in python  -->  PyQt,PySide,Kivy,wxPython
#fetch number of photos from os module and put in twinter canvas-->challange
