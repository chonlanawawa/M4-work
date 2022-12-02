from tkinter import*
from tkinter import ttk

root = Tk()
root.title("ComboBox Test")
root.option_add("*font","PSL-omyim 20")

Label(root,text="โปรแกรมสูตรคูณ",fg="blue",bg="lightblue")\
    .grid(row=0,column=0,columnspan=2,sticky=NSEW)
Label(root,text="ตัวเลขที่1",justify=LEFT,fg="green")\
    .grid(row=1,column=0)
Label(root,text="ตัวเลขที่2",justify=LEFT,fg="red")\
    .grid(row=2,column=0)

num1 = StringVar(value="ระบุตัวเลขที่1")
value_num1 = [1,2,3,4,5,6,7,8,9,10,11,12]
num2 = StringVar(value = "ระบุตัวเลขที่2")
value_num2 = list(range(1,13))

valuenum1_str = ["1","2","3","4","5","6","7","8","9","10","11","12"]
valuenum2_str = ["1","2","3","4","5","6","7","8","9","10","11","12"]

cb1 = ttk.Combobox(root,values=value_num1,textvariable=num1,justify=CENTER,width=15,state="readonly")
cb1.grid(row=1,column=1,sticky=NSEW)

cb2 = ttk.Combobox(root,values=value_num2,textvariable=num2,justify=CENTER,width=15,state="readonly")
cb2.grid(row=2,column=1,sticky=NSEW)

show = StringVar(value="ผลลัพธ์")

label1=Label(root,fg="blue",bg="lightblue",textvariable=show)
label1.grid(row=4,columnspan=2,sticky=NSEW)

def on_click():
    num_1,num_2 = num1.get(),num2.get()
    if valuenum1_str.__contains__(num_1) and valuenum2_str.__contains__(num_2):
        result = int(num_1) * int(num_2)
        label1.config(bg="red",fg="white")
        show.set(f"{num_1} * {num_2} = {result}")
        print(f"{num_1} * {num_2} = {result}")
    else: 
        show.set(f"กรุณาระบุตัวเลข")
        label1.config(bg="red",fg="white")

btn1 = Button(root,text="คำนวณ",fg="blue",command=on_click)
btn1.grid(row=3,column=1,sticky=NSEW)

def cancel():
    show.set(f"ผลลัพธ์")
    label1.config(bg="lightblue",fg="blue")
    num1.set(f"ระบุตัวเลขที่1")
    num2.set(f"ระบุตัวเลขที่2")

btn2 = Button(root,text="ยกเลิก",fg="purple",command=cancel)
btn2.grid(row=3,column=0,sticky=NSEW)

root.mainloop()