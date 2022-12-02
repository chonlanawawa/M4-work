from tkinter import*
root = Tk()
root.title("ชื่อร้าน")
root.option_add("*font","PSL-omyim 22")

label1=Label(text="ชื่อร้าน",bg="lightblue",fg="black")
label1.grid(row=0,columnspan=3,sticky=NSEW)

label2=Label(text="รายการอาหารที่สั่ง",fg="red",bg="orange")
label2.grid(row=0,column=4,columnspan=5,sticky=NSEW)

label3=Label(text="เริ่มต้นบันทึกรายการอาหารที่สั่ง",fg="black",bg="yellow")
label3.grid(row=1,column=4,columnspan=5,rowspan=3,sticky=NSEW)

btnfin=Button(text="ยกเลิกรายการ หรือ เริ่มต้นใหม่",fg="red")
btnfin.grid(row=3,column=4,columnspan=5,sticky=S)

photo1 = PhotoImage(file="D:/chonlana/pizza.png")
photo2 = PhotoImage(file="D:/chonlana/soup.png")
photo3 = PhotoImage(file="D:/chonlana/spaghetti.png")
photo4 = PhotoImage(file="D:/chonlana/burger.png")
photo5 = PhotoImage(file="D:/chonlana/frenchfries.png")
photo6 = PhotoImage(file="D:/chonlana/salmon.png")
photo7 = PhotoImage(file="D:/chonlana/hotdog.png")
photo8 = PhotoImage(file="D:/chonlana/steak.png")
photo9 = PhotoImage(file="D:/chonlana/salad.png")


btn1=Button(text="pizza",fg="blue",image=photo1,compound=TOP)
btn1.grid(column=0,row=1,sticky=NSEW)

btn2=Button(text="soup",fg="blue",image=photo2,compound=TOP)
btn2.grid(column=1,row=1,sticky=NSEW)

btn3=Button(text="spaghetti",fg="blue",image=photo3,compound=TOP)
btn3.grid(column=2,row=1,sticky=NSEW)

btn4=Button(text="burger",fg="blue",image=photo4,compound=TOP)
btn4.grid(column=0,row=2,sticky=NSEW)

btn5=Button(text="frenchfries",fg="blue",image=photo5,compound=TOP)
btn5.grid(column=1,row=2,sticky=NSEW)

btn6=Button(text="salmon",fg="blue",image=photo6,compound=TOP)
btn6.grid(column=2,row=2,sticky=NSEW)

btn7=Button(text="hotdog",fg="blue",image=photo7,compound=TOP)
btn7.grid(column=0,row=3,sticky=NSEW)

btn8=Button(text="steak",fg="blue",image=photo8,compound=TOP)
btn8.grid(column=1,row=3,sticky=NSEW)

btn9=Button(text="salad",fg="blue",image=photo9,compound=TOP)
btn9.grid(column=2,row=3,sticky=NSEW)

root.mainloop()