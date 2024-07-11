from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("anchal Canvas")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

#the line goes from the point to point(x1,y1 - x2,y2)
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")
#top-left  to  bottom-right for rectangle
can_widget.create_rectangle(3,5,700,300)
#write text under canvas
can_widget.create_text(400,200,text="I love my life")
#draw oval top-left to bottom-left
can_widget.create_oval(3,5,700,300)
root.mainloop()