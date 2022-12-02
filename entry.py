from tkinter import *

root = Tk()
root.title("Login Test")
root.option_add("*font","PSL-omyim 20")

Label(root,text="Please Login",fg="gold",bg="black")\
    .grid(row=0,columnspan=2,sticky=NSEW)
Label(root,text="Username :",justify=LEFT,fg="blue")\
    .grid(row=1,column=0)
Label(root,text="Password :",justify=LEFT,fg="red")\
    .grid(row=2,column=0)

username = StringVar(value = "Your username")
password = StringVar()
Entry(root,textvariable=username,justify=RIGHT)\
    .grid(row=1,column=1)
Entry(root,textvariable=password,justify=RIGHT,show="*")\
    .grid(row=2,column=1)

textshow = StringVar()

def login():
    if username.get() == "wawa" and password.get() == "wawawawa":
        textshow.set("Welcome Wawa")
        labeltextshow = Label(root,textvariable=textshow,fg="blue",bg="lightblue")
        labeltextshow.grid(row=4,columnspan=2,sticky=NSEW)
    else:
        textshow.set("Please try again")
        labeltextshow = Label(root,textvariable=textshow,fg="white",bg="red")
        labeltextshow.grid(row=4,columnspan=2,sticky=NSEW)

Button(root,text="Login",bg="lightgreen",fg="green",command=login)\
    .grid(row=3,columnspan=2,sticky=NSEW)


root.mainloop()