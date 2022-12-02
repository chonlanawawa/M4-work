from tkinter import *
root = Tk()
root.geometry("500x500") 
Label1 = Label(text="aaa",bg="green")
Label1.grid(row=0,column=0,ipadx=50,ipady=50)

Label2 = Label(text="aaa",bg="blue")
Label2.grid(row=1,column=1)

Label3 = Label(text="aaa",bg="red")
Label3.grid(row=2,column=2)

Label4 = Label(text="aa",bg="yellow")
Label4.grid(sticky=E)

root.mainloop()