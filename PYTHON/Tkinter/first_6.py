from tkinter import *
def getvalue():
    #  a=uservalue.get()
    #  b=passvalue.get()
    #  print(uservalue.get())
    #  print(passvalue.get())
    print(f"{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{Emercontactvalue.get()},{paymodevalue.get()},{foodservalue.get()}\n")
    # to save in a file
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{Emercontactvalue.get()},{paymodevalue.get()},{foodservalue.get()}\n")

root=Tk()
root.geometry("644x344")
Label(root,text="welcome to anchal page",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
#text form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
Emercontact=Label(root,text="Emergency Contact")
paymode=Label(root,text="Payment Mode")
#paking the text form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
Emercontact.grid(row=4,column=2)
paymode.grid(row=5,column=2)
#take input for value
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
Emercontactvalue=StringVar()
paymodevalue=StringVar()
foodservalue=IntVar()
#entries for form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
Emerentry=Entry(root,textvariable=Emercontactvalue)
payentry=Entry(root,textvariable=paymodevalue)
#paking the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
Emerentry.grid(row=4,column=3)
payentry.grid(row=5,column=3)
#checkbox & packing
foodservice=Checkbutton(text="Want to prebook your meal?",variable=foodservalue)
foodservice.grid(row=6,column=3)
#button & packing it and assingning command
Button(text="Submit to travels",command=getvalue).grid(row=7,column=3)
root.mainloop()