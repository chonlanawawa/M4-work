from tkinter import *
root = Tk()
root.title("HOMEWORK-GUI")

label1=Label(bg="yellow",text='NAME:')
label1.grid(row=0,column=0,ipadx=231.5,ipady=15)

label2=Label(bg="green",text="MAJOR")
label2.grid(row=1,column=0,ipadx=230,ipady=15)

label_space=Label()
label_space.grid(row=2,column=0,ipady=55)

label3=Label(bg="pink")
label3.place(x=25,y=103,height=110,width=110)
label4=Label(bg="red")
label4.place(x=155,y=103,height=110,width=110)
label5=Label(bg="pink")
label5.place(x=285,y=103,height=110,width=110)
label6=Label(bg="red")
label6.place(x=415,y=103,height=110,width=110)

label7=Label(text="SPSM",bg="white")
label7.grid(row=3,column=0,ipadx=232,ipady=15)

label8=Label(text="OK",fg="white",bg="black")
label8.grid(row=4,column=0,ipadx=65,ipady=15,pady=10)

root.mainloop()

