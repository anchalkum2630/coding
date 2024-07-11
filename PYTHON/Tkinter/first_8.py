from tkinter import *
def harry(event):
    print(f"you clicked on buttonm at {event.x},{event.y}")
root=Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

Widget=Button(root,text="click me please")
Widget.pack()

Widget.bind('<Button-1>',harry)
Widget.bind('<Double-1>',quit)

root.mainloop()