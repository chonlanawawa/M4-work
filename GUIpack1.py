from tkinter import *
root = Tk()
root.geometry("300x300")

Label1 = Label(text="Test GUI",bg='blue')
Label2 = Label(text="Chonlana",bg="purple")
Label3 = Label(text="a",bg="green")
Label4 = Label(text="Test GUI",bg="red")
Label5 = Label(text="c",bg="orange")

Label1.pack(side=LEFT,fill=BOTH)
Label4.pack(side=RIGHT,fill=BOTH)
Label2.pack(side=TOP,fill=BOTH,expand=True)
Label3.pack(side=BOTTOM,fill=BOTH,expand=True)
Label5.place(x=150,y=150)

root.mainloop()