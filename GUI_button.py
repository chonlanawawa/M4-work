from tkinter import*
root = Tk()
root.title("Science Test")
root.option_add("*font","PSL-omyim 30")

def  countclick_correct():
    global count
    count += 1
    total_point.set(f"Total point: {count}")

def  countclick_wrong():
    global count
    count -= 1
    total_point.set(f"Total point: {count}")

def finish():
    root.destroy()
    root2 = Tk()
    root2.title("รายงานผลคะแนนทั้งหมด")
    root2.option_add("*font","Hack 30")
    root2.geometry("300x70")
    Label(root2,text=f"Total point: {count}",fg="purple",width=34).pack()
    root2.mainloop

label1=Label(text="1.ดวงอาทิตย์ขึ้นทางทิศอะไร",bg="orange")
label1.grid(row=0,columnspan=5,sticky=NSEW)
label2=Label(text="ให้นักเรียนเลือกคำตอบด้านล่าง",bg="lightblue",font="PSL-omyim 20")
label2.grid(row=1,columnspan=5,sticky=NSEW)

photo1 = PhotoImage(file="north.png")
photo2 = PhotoImage(file="east.png")
photo3 = PhotoImage(file="west.png")
photo4 = PhotoImage(file="south.png")

button1=Button(text="ก. ทิศเหนือ",bg="orange",fg="red",image=photo1,compound=TOP,command=countclick_wrong)
button1.grid(row=2,column=0)
button2=Button(text="ข. ทิศตะวันออก",bg="orange",fg="red",image=photo2,compound=TOP,command=countclick_correct)
button2.grid(row=2,column=1)
button3=Button(text="ค. ทิศตะวันตก",bg="orange",fg="red",image=photo3,compound=TOP,command=countclick_wrong)
button3.grid(row=2,column=2)
button4=Button(text="ง. ทิศใต้",bg="orange",fg="red",image=photo4,compound=TOP,command=countclick_wrong)
button4.grid(row=2,column=3)

total_point= StringVar()
total_point.set("Total point: 0")
count=0

btn_point=Button(textvariable=total_point,fg="purple",width=34)
btn_point.grid(row=3,columnspan=5,sticky=NSEW)       

btn_finish=Button(text="Finish",fg="blue",command=finish)
btn_finish.grid(row=4,column=0,columnspan=5)

root.mainloop()