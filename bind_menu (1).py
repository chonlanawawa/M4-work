from tkinter import*
from datetime import datetime

root = Tk()
root.title("ชื่อร้าน")
root.option_add("*font","Hack 20")

def choose_menu(e):
    global totalmenu,allmenu,menuitem,menu,totalprice
    menuitem = e.widget.cget("text")
    totalprice += menu[menuitem]
    price.set(f"รายการอาหารทั้งหมด เท่ากับ {totalprice} บาท")
    allmenu += menuitem+" ราคา "+str(menu[menuitem])+" บาท\n"
    totalmenu.set(f"รายการอาหารที่เลือก คือ \n{allmenu}")

def mouse_enter(event):
    event.widget["fg"]="green"

def mouse_leave(event):
    event.widget["fg"]="black"

def cancel():
    global totalmenu,totalprice,allmenu
    price.set(f"รายการอาหารทั้งหมด เท่ากับ 0 บาท")
    totalmenu.set(f"เริ่มต้นบันทึกรายการอาหารใหม่")
    totalprice = 0
    allmenu = " "

def exit():
    root.destroy()

def print_bills():
    global totalmenu,allmenu,totalprice
    totalmenu.set(f"บันทึกเรียบร้อยแล้ว")
    print(datetime.now())
    print("-------------\n")
    print("รายการอาหารทั้งหมด\n")
    print(allmenu)
    print("-------------")
    print(f"รวมเป็นเงิน {totalprice} บาท")

menu = {"pizza":200,"soup":50,"spaghetti":80,"burger":99,"frenchfries":80,"salmon":150}
totalmenu= StringVar()
price = StringVar()
times = StringVar()
times.set(datetime.now())
totalmenu.set(f"เริ่มต้นบันทึกรายการอาหารที่สั่ง")
price.set(f"รายการอาหารที่เลือก")
allmenu = " "
totalprice = 0

restaurant = Label(root, text="ชื่อร้าน",fg="orange",bg="red")
restaurant.grid(row=0,columnspan=3,sticky=NSEW)
cashier_time = Label(root,textvariable=times,fg="red",bg="orange")
cashier_time.grid(row=1,columnspan=3,sticky=NSEW)

photo1 = PhotoImage(file="pizza_bind.png")
photo2 = PhotoImage(file="soup_bind.png")
photo3 = PhotoImage(file="spaghetti_bind.png")
photo4 = PhotoImage(file="burger_bind.png")
photo5 = PhotoImage(file="frenchfries_bind.png")
photo6 = PhotoImage(file="salmon_bind.png")

menu1 = Button(root,text="pizza",image=photo1,compound=TOP)
menu1.grid(row=2,column=0,sticky=NSEW)
menu2 = Button(root,text="soup",image=photo2,compound=TOP)
menu2.grid(row=2,column=1,sticky=NSEW)
menu3 = Button(root,text="spaghetti",image=photo3,compound=TOP)
menu3.grid(row=2,column=2,sticky=NSEW)
menu4 = Button(root,text="burger",image=photo4,compound=TOP)
menu4.grid(row=3,column=0,sticky=NSEW)
menu5 = Button(root,text="frenchfries",image=photo5,compound=TOP)
menu5.grid(row=3,column=1,sticky=NSEW)
menu6 = Button(root,text="salmon",image=photo6,compound=TOP)
menu6.grid(row=3,column=2,sticky=NSEW)

menu1.bind("<Button-1>",choose_menu)
menu2.bind("<Button-1>",choose_menu)
menu3.bind("<Button-1>",choose_menu)
menu4.bind("<Button-1>",choose_menu)
menu5.bind("<Button-1>",choose_menu)
menu6.bind("<Button-1>",choose_menu)

menu1.bind("<Enter>",mouse_enter)
menu2.bind("<Enter>",mouse_enter)
menu3.bind("<Enter>",mouse_enter)
menu4.bind("<Enter>",mouse_enter)
menu5.bind("<Enter>",mouse_enter)
menu6.bind("<Enter>",mouse_enter)

menu1.bind("<Leave>",mouse_leave)
menu2.bind("<Leave>",mouse_leave)
menu3.bind("<Leave>",mouse_leave)
menu4.bind("<Leave>",mouse_leave)
menu5.bind("<Leave>",mouse_leave)
menu6.bind("<Leave>",mouse_leave)

report_menu = Label(root,textvariable=totalmenu,fg="red",bg="orange")
report_menu.grid(row=4,columnspan=4,sticky=NSEW)
bill = Label(root,textvariable=price,fg="orange",bg="red")
bill.grid(row=5,columnspan=4,sticky=NSEW)
cancel_all = Button(root,text="ยกเลิกรายการ",fg="red",command=cancel)
cancel_all.grid(row=6,column=0,sticky=NSEW)
exit_all = Button(root,text="Exit",fg="blue",command=exit)
exit_all.grid(row=6,column=1,sticky=NSEW)
bill_all = Button(root,text="บันทึกรายการที่สั่ง",fg="purple",command=print_bills)
bill_all.grid(row=6,column=2,sticky=NSEW)

root.mainloop()