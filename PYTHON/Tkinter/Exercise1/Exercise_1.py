#3 pics and 3 news make newspaper
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Newspaper")
root.geometry("1000x800")
texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt","r",encoding="utf-8") as f:
         text=f.read()
         texts.append(text)
    image=Image.open(f"pic_{i+1}.jpg")
    #TODO: resize the image
    image=image.resize((225,225))
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(root,width=800,height=70)
Label(f0,text="code with anchal",font="lucida 33 bold").pack()
Label(f0,text="January 19, 2024",font="lucida 13 bold").pack()
f0.grid(row=1)

f1=Frame(root,width=900,height=200)
Label(f1,text=texts[0]).pack(side="left")
Label(f1,text=photos[0]).pack(side="right")
f1.grid(row=2)
root.mainloop()