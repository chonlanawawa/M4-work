from tkinter import *
root = Tk()
root.option_add("*font","Hack 30")
root.geometry("500x300+1000+300")

def on_click(event):
    event.widget["text"]="on_click"
def middle_click(event):
    event.widget["text"]="middle_click"
def right_click(event):
    event.widget["text"]="right_click"
def mouse_enter(event):
    event.widget["fg"]="blue"
def mouse_leave(event):
    event.widget["fg"]="green"
def doubleclick(event):
    event.widget["text"]="double_click"
def doubleright(event):
    event.widget["text"]="double_rightclick"
def doublemiddle(event):
    event.widget["text"]="double_middleclick"
def key_enter(event):
    event.widget["text"]="enter"

button1 = Button(text="Bind event")
button1.pack(expand=True)

button1.bind("<Button-1>",on_click)
button1.bind("<Button-2>",middle_click)
button1.bind("<Button-3>",right_click)
button1.bind("<Enter>",mouse_enter)
button1.bind("<Leave>",mouse_leave)
button1.bind("<Double-1>",doubleclick)
button1.bind("<Double-2>",doublemiddle)
button1.bind("<Double-3>",doubleright)
button1.bind("<Return>",key_enter)


root.mainloop()