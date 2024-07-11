from tkinter import *
root=Tk()
root.geometry("950x550")
root.title("My GUI With Anchal")

#important label option
# text->adds the Text
# bd-> background
# fg-> foreground
# font->sets the Font  ("arial",10,"bold","italic")) or "arial 10 bold italic"
# padx->x padding
# pady-> y padding
# relief-> border styling -SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[22] is a country in South Asia. It is the seventh-largest country by\n area; the most populous country as of June 2023;[23][24] and from the time of its independence in 1947, \nthe world's most populous democracy.[25][26][27]\n Bounded by the Indian Ocean on the south, the Arabian Sea\n on the southwest, and the Bay of Bengal on the southeast\n, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north;\n and Bangladesh and Myanmar[k] to the east. In the Indian Ocean, India is in the vicinity\n of Sri Lanka and the\n Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.''',bg="lightpink",fg="black",padx=60,pady=50,font=("arial",10,"bold","italic"),borderwidth=4,relief=SUNKEN)


#important pack option
'''
anchor = north,west,east,south(ne,nw,sw,se)
side = top,bottom,left,right
fill = 
padx=
pady=


'''
title_label.pack(anchor="center",side="top",fill="x",padx=10,pady=20)

root.mainloop()

