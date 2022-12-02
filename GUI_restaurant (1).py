from tkinter import*
root = Tk()
root.title("ชื่อร้าน")
root.option_add("*font","PSL-omyim 30")

def  menu1():
    global price
    price += 200
    total_price.set(f"Total price: {price}")
    global allmenu
    allmenu += "\npizza"
    total_menu.set(f"Total menu: {allmenu}")

def  menu2():
    global price
    price += 100
    total_price.set(f"Total price: {price}")
    global allmenu
    allmenu += "\nsalad"
    total_menu.set(f"Total menu: {allmenu}")

def  menu3():
    global price
    price += 100
    total_price.set(f"Total price: {price}")
    global allmenu
    allmenu += "\nburger"
    total_menu.set(f"Total menu: {allmenu}")

def  menu4():
    global price
    price += 150
    total_price.set(f"Total price: {price}")
    global allmenu
    allmenu += "\nspaghetti"
    total_menu.set(f"Total menu: {allmenu}")

def finish():
    root.destroy()
    root2 = Tk()
    root2.title("รายการอาหารทั้งหมด")
    root2.option_add("*font","Hack 30")
    Label(root2,text=f"Total price: {price}",fg="purple",width=34).pack()
    Label(root2,text=f"Total menu:{allmenu}",fg="blue",width=34).pack()
    root2.mainloop()

label1=Label(text="ชื่อร้าน",bg="red",fg="orange")
label1.grid(row=0,columnspan=5,sticky=NSEW)

label2=Label(text="รายการอาหาร",bg="orange")
label2.grid(row=1,columnspan=5,sticky=NSEW)

photo1 = PhotoImage(file="pizza.png")
photo2 = PhotoImage(file="salad.png")
photo3 = PhotoImage(file="burger.png")
photo4 = PhotoImage(file="spaghetti.png")

button1=Button(text="pizza",bg="lightblue",fg="blue",image=photo1,compound=TOP,command=menu1)
button1.grid(row=2,column=0)
button2=Button(text="salad",bg="lightblue",fg="blue",image=photo2,compound=TOP,command=menu2)
button2.grid(row=2,column=1)
button3=Button(text="burger",bg="lightblue",fg="blue",image=photo3,compound=TOP,command=menu3)
button3.grid(row=2,column=2)
button4=Button(text="spaghetti",bg="lightblue",fg="blue",image=photo4,compound=TOP,command=menu4)
button4.grid(row=2,column=3)

total_price= StringVar()
total_price.set("Total price: 0") 
price=0

total_menu= StringVar()
total_menu.set("Total menu:")
allmenu=" "

btn_menu=Button(textvariable=total_menu,fg="orange",width=34,bg="red")
btn_menu.grid(row=3,columnspan=5,sticky=NSEW)    

btn_price=Button(textvariable=total_price,fg="red",width=34,bg="orange")
btn_price.grid(row=4,columnspan=5,sticky=NSEW)       

btn_finish=Button(text="Finish",fg="blue",command=finish,bg="lightblue")
btn_finish.grid(row=5,column=0,columnspan=5)

root.mainloop()

