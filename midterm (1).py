#ส่งไฟล์อีกรอบนึงค่ะ😭

from tkinter import *
from datetime import datetime
import requests

root = Tk()
root.title("coffee shop")
root.option_add("*font","Times 20")

def choose(e):
    global ordered_menu,menuitem
    menuitem = e.widget.cget("text")
    ordered_menu.set(f"เครื่องดื่มที่สั่ง คือ {menuitem}")

def mouse_enter(event):
    event.widget["fg"]="#ad8366"

def mouse_leave(event):
    event.widget["fg"]="#612d14"

def cancel():
    global ordered_menu,price,menu,total_price
    ordered_menu.set(f"เริ่มต้นบันทึกรายการเครื่องดื่มใหม่")
    price = 0
    menu = " "

def save_menu():
    root.destroy()
    root2=Tk()
    root2.title("รายละเอียดเพิ่มเติม")
    root2.option_add("*font","Times 20")

    ordered_sugar=StringVar()
    ordered_category=StringVar()
    price = 0
    total_price=StringVar()
    menu_price = {"espresso":30,"americano":30,"latte":35,"cappuccino":40,"mocha":40,"chocolate":40}

    def mouse_enter2(event):
     event.widget["fg"]="#ad8366"

    def mouse_leave2(event):
     event.widget["fg"]="#612d14"

    def set_normal_price(price,total_price,menu_price):
        price += menu_price[menuitem]
        total_price.set(f"ราคาเครื่องดื่มทั้งหมด {price} บาท")
    set_normal_price(price,total_price,menu_price)
 
    def type(e,price=menu_price[menuitem]):
      order_type = e.widget["text"]
      if order_type == "ร้อน":
        category = " "
        category += "ร้อน"
        price = 0
      elif order_type == "เย็น":
        category = " "
        category += "เย็น"
        price = 0
      elif order_type == "ปั่น":
        category = " "
        category += "ปั่น"
        price = 5
      total_price.set(f"ราคาเครื่องดื่มทั้งหมด {price+menu_price[menuitem]} บาท")
      ordered_category.set(f"เครื่องดื่ม:{category}")

    def sweetness(e):
      order_sweet = e.widget["text"]
      if order_sweet == "0%":
        sugar = " "
        sugar += "0%"
      elif order_sweet == "25%":
        sugar = " "
        sugar += "25%"
      elif order_sweet == "50%":
        sugar = " "
        sugar += "50%"
      elif order_sweet == "75%":
        sugar = " "
        sugar += "75%"
      elif order_sweet == "100%":
        sugar = " "
        sugar += "100%"
      ordered_sugar.set(f"ความหวาน{sugar}")
      return ordered_sugar

    label_2 = Label(root2,text="เครื่องดื่มที่สั่งคือ "+menuitem,fg="#ebd9bc",bg="#612d14")
    label_2.grid(row=0,columnspan=8,sticky=NSEW)
    label2_2 = Label(root2,text="ระบุรายละเอียดเพิ่มเติม",bg="#ebd9bc",fg="#612d14")
    label2_2.grid(row=1,columnspan=8,sticky=NSEW)

    label_type = Label(root2,text="ประเภท",fg="#ebd9bc",bg="#612d14")
    label_type.grid(row=2,column=0,sticky=NSEW)
    label_sweet = Label(root2,text="ความหวาน",bg="#ebd9bc",fg="#612d14")
    label_sweet.grid(row=3,column=0,sticky=NSEW)

    label_color = Label(root2,bg="#612d14")
    label_color.grid(row=2,column=4,columnspan=5,sticky=NSEW)

    label_price = Label(root2,textvariable=(total_price),fg="#ebd9bc",bg="#612d14")
    label_price.grid(row=5,columnspan=8,sticky=NSEW)
    label_details = Label(root2,text="รายละเอียดเพิ่มเติม",bg="#ebd9bc",fg="#612d14")
    label_details.grid(row=6,columnspan=8,sticky=NSEW)

    label_sugar = Label(root2,textvariable=(ordered_sugar),fg="#ebd9bc",bg="#612d14")
    label_sugar.grid(row=7,columnspan=8,sticky=NSEW)
    label_type = Label(root2,textvariable=(ordered_category),fg="#ebd9bc",bg="#612d14")
    label_type.grid(row=8,columnspan=8,sticky=NSEW)

    btn1_type = Button(root2,text="ร้อน",fg="#612d14")
    btn1_type.grid(row=2,column=1,sticky=NSEW)
    btn2_type = Button(root2,text="เย็น",fg="#612d14")
    btn2_type.grid(row=2,column=2,sticky=NSEW)
    btn3_type = Button(root2,text="ปั่น",fg="#612d14")
    btn3_type.grid(row=2,column=3,sticky=NSEW)

    btn1_sweet = Button(root2,text="0%",fg="#612d14")
    btn1_sweet.grid(row=3,column=1,sticky=NSEW)
    btn2_sweet = Button(root2,text="25%",fg="#612d14")
    btn2_sweet.grid(row=3,column=2,sticky=NSEW)
    btn3_sweet = Button(root2,text="50%",fg="#612d14")
    btn3_sweet.grid(row=3,column=3,sticky=NSEW)
    btn4_sweet = Button(root2,text="75%",fg="#612d14")
    btn4_sweet.grid(row=3,column=4,sticky=NSEW)
    btn5_sweet = Button(root2,text="100%",fg="#612d14")
    btn5_sweet.grid(row=3,column=5,sticky=NSEW)

    btn1_type.bind("<Enter>",mouse_enter2)
    btn2_type.bind("<Enter>",mouse_enter2)
    btn3_type.bind("<Enter>",mouse_enter2)
    btn1_sweet.bind("<Enter>",mouse_enter2)
    btn2_sweet.bind("<Enter>",mouse_enter2)
    btn3_sweet.bind("<Enter>",mouse_enter2)
    btn4_sweet.bind("<Enter>",mouse_enter2)
    btn5_sweet.bind("<Enter>",mouse_enter2)

    btn1_type.bind("<Leave>",mouse_leave2)
    btn2_type.bind("<Leave>",mouse_leave2)
    btn3_type.bind("<Leave>",mouse_leave2)
    btn1_sweet.bind("<Leave>",mouse_leave2)
    btn2_sweet.bind("<Leave>",mouse_leave2)
    btn3_sweet.bind("<Leave>",mouse_leave2)
    btn4_sweet.bind("<Leave>",mouse_leave2)
    btn5_sweet.bind("<Leave>",mouse_leave2)

    btn1_type.bind("<Button-1>",type)
    btn2_type.bind("<Button-1>",type)
    btn3_type.bind("<Button-1>",type)

    btn1_sweet.bind("<Button-1>",sweetness)
    btn2_sweet.bind("<Button-1>",sweetness)
    btn3_sweet.bind("<Button-1>",sweetness)
    btn4_sweet.bind("<Button-1>",sweetness)
    btn5_sweet.bind("<Button-1>",sweetness)

    message_line=(f"{ordered_menu.get()} {total_price.get()} และรายละเอียดเพิ่มเติมดังนี้ {ordered_category.get()} และ {ordered_sugar.get()}")
    def lineNotify(message):
     payload = {"message":message}
     return _lineNotify(payload)

    def _lineNotify(payload,file=None):
     import requests
     url = 'https://notify-api.line.me/api/notify'
     token = 'VwkmW4iQE2wine1k7EEEaNDegWNln4V27qxAMLjvLCg'
     headers = {'Authorization':'Bearer '+token}
     return requests.post(url=url, headers=headers, data=payload, files=file)
 
    def line(): 
     global message_line
     message_line=(f"{ordered_menu.get()} {total_price.get()} และรายละเอียดเพิ่มเติมดังนี้ {ordered_category.get()} และ {ordered_sugar.get()}")
     lineNotify(message_line)

    btnfinish=Button(root2,text="บันทึกรายการและส่งรายการแจ้งเตือน",fg="#612d14",command=line)
    btnfinish.grid(row=9,columnspan=10,sticky=NSEW)

    root2.mainloop()

dtdate = datetime.now().strftime("%d/%m/%Y")
dttime = datetime.now().strftime("%H:%M:%S")

ordered_menu=StringVar()
ordered_menu.set(f"เริ่มต้นบันทึกรายการเครื่องดื่มที่สั่ง")

photo1 = PhotoImage(file="espresso.png")
photo2 = PhotoImage(file="americano.png")
photo3 = PhotoImage(file="latte.png")
photo4 = PhotoImage(file="cappuccino.png")
photo5 = PhotoImage(file="mocha.png")
photo6 = PhotoImage(file="chocolate.png")

label = Label(root,text="Coffee Shop",fg="#ebd9bc",bg="#612d14")
label.grid(row=0,columnspan=5,sticky=NSEW)
label2 = Label(root,text="Menu: สั่งเครื่องดื่มได้ครั้งละรายการ",bg="#ebd9bc",fg="#612d14")
label2.grid(row=1,columnspan=5,sticky=NSEW)
label3 = Label(root,text=("วันที่และเวลาปัจจุบัน "+dtdate+" , "+dttime),fg="#ebd9bc",bg="#612d14")
label3.grid(row=2,columnspan=5,sticky=NSEW)

def tick():
    global curtime
    curtime = datetime.now().time()
    ftime = curtime.strftime("%H:%M:%S")
    label3.config(text="วันที่และเวลาปัจจุบัน "+dtdate+" , "+ftime)
    label3.after(1000,tick)
tick()

label4=Label(root,textvariable=ordered_menu,fg="#ebd9bc",bg="#612d14")
label4.grid(row=5,columnspan=5,sticky=NSEW)

btn1 = Button(root,text="ยกเลิกรายการที่สั่ง",fg="#612d14",command=cancel)
btn1.grid(row=6,column=0,sticky=NSEW)
btn2 = Button(root,text="บันทึกรายการที่สั่งและไปหน้าต่อไป",fg="#612d14",command=save_menu)
btn2.grid(row=6,column=1,columnspan=2,sticky=NSEW)

menu1 = Button(root,text="espresso",image=photo1,compound=TOP,fg="#612d14")
menu1.grid(row=3,column=0,sticky=NSEW)
menu2 = Button(root,text="americano",image=photo2,compound=TOP,fg="#612d14")
menu2.grid(row=3,column=1,sticky=NSEW)
menu3 = Button(root,text="latte",image=photo3,compound=TOP,fg="#612d14")
menu3.grid(row=3,column=2,sticky=NSEW)
menu4 = Button(root,text="cappuccino",image=photo4,compound=TOP,fg="#612d14")
menu4.grid(row=4,column=0,sticky=NSEW)
menu5 = Button(root,text="mocha",image=photo5,compound=TOP,fg="#612d14")
menu5.grid(row=4,column=1,sticky=NSEW)
menu6 = Button(root,text="chocolate",image=photo6,compound=TOP,fg="#612d14")
menu6.grid(row=4,column=2,sticky=NSEW)

menu1.bind("<Button-1>",choose)
menu2.bind("<Button-1>",choose)
menu3.bind("<Button-1>",choose)
menu4.bind("<Button-1>",choose)
menu5.bind("<Button-1>",choose)
menu6.bind("<Button-1>",choose)

menu1.bind("<Enter>",mouse_enter)
menu2.bind("<Enter>",mouse_enter)
menu3.bind("<Enter>",mouse_enter)
menu4.bind("<Enter>",mouse_enter)
menu5.bind("<Enter>",mouse_enter)
menu6.bind("<Enter>",mouse_enter)
btn1.bind("<Enter>",mouse_enter)
btn2.bind("<Enter>",mouse_enter)

menu1.bind("<Leave>",mouse_leave)
menu2.bind("<Leave>",mouse_leave)
menu3.bind("<Leave>",mouse_leave)
menu4.bind("<Leave>",mouse_leave)
menu5.bind("<Leave>",mouse_leave)
menu6.bind("<Leave>",mouse_leave)
btn1.bind("<Leave>",mouse_leave)
btn2.bind("<Leave>",mouse_leave)

root.mainloop()