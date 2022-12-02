from tkinter import *
from tkinter import messagebox
root = Tk()

root.title("Radiobutton Test") 
root.option_add("*font","PSL-omyim 20")

col_n = 3
label1 = Label(root,text="จังหวัดที่นักเรียนอยากไปท่องเที่ยวมากที่สุด",fg="black",bg="gold")
label1.grid(row=0,column=0,columnspan=col_n,sticky=NSEW)

list_travel = ["กรุงเทพ","ชลบุรี","เลย","ภูเก็ต","พังงา","เชียงใหม่"]
value = ["กรุงเทพที่มีประชากรมากที่สุดในประเทศ","ชลบุรีที่มีหาดพัทยาที่สวยงาม","เลยที่มีภูเขาล้อมรอบ","ภูเก็ตแหล่งท่องเที่ยวระดับโลก","พังงาเมืองที่มีทั้งภูเขาและทะเล","เชียงใหม่ที่มีพระธาตุดอยสุเทพ"]

show = StringVar(value="ผลลัพธ์")
vg = StringVar()
vg.set(0)

def on_click():
    show.set(f"คุณได้เลือกจังหวัด\n {vg.get()}")

for i in range(len(list_travel)):
    rd = Radiobutton(root,text=list_travel[i],variable=vg,value=value[i],width=10,indicatoron=True,command=on_click)
    rd.grid(row=i//col_n+1,column=i % col_n,sticky=NSEW)

label2 = Label(root,textvariable=show,fg="blue",bg="lightblue",width=20,height=2,wraplength=500)
label2.grid(row=5,column=0,columnspan=col_n,sticky=NSEW)

def exit():
    confirm = messagebox.askquestion("ยืนยัน","คุณต้องการออกจากโปรแกรมใช่หรือไม่")
    if confirm == "yes":
        root.destroy()

def show_warning():
    messagebox.showwarning("Warning","ได้ทำการบันทึกข้อมูลเรียบร้อยแล้ว")

def show_info():
    messagebox.showinfo("รายละเอียด","โปรแกรมนี้เป็นโปรแกรมทดสอบการใช้messagebox")

btn1 = Button(root,text="ออกจากโปรแกรม",command=exit)
btn1.grid(row=6,column=0,sticky=NSEW)
btn2 = Button(root,text="บันทึกข้อมูล",command=show_warning)
btn2.grid(row=6,column=1,sticky=NSEW)
btn3 = Button(root,text="รายละเอียดโปรแกรม",command=show_info)
btn3.grid(row=6,column=2,sticky=NSEW)

root.mainloop()