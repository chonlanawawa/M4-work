# VwkmW4iQE2wine1k7EEEaNDegWNln4V27qxAMLjvLCg
from tkinter import *
from datetime import datetime

root = Tk()
root.title = "score board"
root.option_add("*font","Hack 20")

team_a_count = 0
team_b_count = 0
total_count = 0
tv_team_a = IntVar()
tv_team_b = IntVar()
tv_total = StringVar()
tv_total.set(f"คะแนนรวมของทั้งสองทีม = {total_count}")

photo1 = PhotoImage(file="D:/Chonlana/liverpool.png")
photo2 = PhotoImage(file="D:/Chonlana/manu.png")
dtdate = datetime.now().strftime("%d/%m/%Y")
dttime = datetime.now().strftime("%H:%M:%S")

label = Label(root,text="Football Score Board",fg="white",bg="black")
label.grid(row=0,columnspan=2,sticky=NSEW)

btn1=Button(root,text="Team_A",image=photo1,compound=TOP,fg="green",padx=70)
btn1.grid(row=1,column=0,ipady=20,sticky=NSEW)
btn2=Button(root,text="Team_B",image=photo2,compound=TOP,fg="red",padx=50)
btn2.grid(row=1,column=1,ipady=20,sticky=NSEW)

label1=Label(root,textvariable=tv_team_a,bg="lightblue")
label1.grid(row=2,column=0,sticky=NSEW)
label2=Label(root,textvariable=tv_team_b,bg="pink")
label2.grid(row=2,column=1,sticky=NSEW)
label3=Label(root,textvariable=tv_total,bg="gold")
label3.grid(row=7,columnspan=2,sticky=NSEW)

def on_click(e):
    global team_a_count,team_b_count,total_count
    score = e.widget["text"]
    if score == "Team_A":
        team_a_count +=1
        tv_team_a.set(team_a_count)
    elif score == "Team_B" :
        team_b_count += 1
        tv_team_b.set(team_b_count)

    total_count += 1
    tv_total.set(f"คะแนนรวมของทั้งสองทีม = {total_count}")

def right_click(e):
    global team_a_count,team_b_count,total_count
    score = e.widget["text"]
    if score == "Team_A":
        team_a_count -= 1
        tv_team_a.set(team_a_count)
    elif score == "Team_B" :
        team_b_count -= 1
        tv_team_b.set(team_b_count)

    total_count -= 1
    tv_total.set(f"คะแนนรวมของทั้งสองทีม = {total_count}")

btn1.bind("<Button-1>",on_click)
btn1.bind("<Button-3>",right_click)
btn2.bind("<Button-1>",on_click)
btn2.bind("<Button-3>",right_click)

label4=Label(root,text=dttime,fg="white",bg="blue")
label4.grid(row=3,columnspan=2,sticky=NSEW)
label5=Label(root,text=("วันที่ปัจจุบัน "+dtdate),bg="green")
label5.grid(row=6,columnspan=2,sticky=NSEW)

def tick():
    global curtime
    curtime = datetime.now().time()
    ftime = curtime.strftime("%H:%M:%S")
    label4.config(text="เวลาปัจจุบัน : "+ftime)
    label4.after(1000,tick)
tick()

label6=Label(root,text="เวลานับถอยหลัง 45:00 นาที",fg="white",bg="red")
label6.grid(row=5,columnspan=2,sticky=NSEW)
t=45*60

def countdown():
    global timer,mins,secs,t,team_a_count,team_b_count
    t -= 1
    mins,secs = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(mins,secs)
    label6.config(text=("เวลานับถอยหลัง : "+timer))
    label6.after(1000,countdown)
countdown()

message_line=(f"ผลการแข่งขันทีม A {team_a_count} และทีม B {team_b_count}")
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
    global meassage_line
    message_line=(f"ผลการแข่งขันทีม A : {team_a_count} คะแนน และทีม B : {team_b_count} คะแนน")
    print(message_line)
    lineNotify(message_line)

btn4=Button(root,text="จบการแข่งขันและส่งรายการแจ้งเตือน",fg="red",command=line)
btn4.grid(row=8,columnspan=2,sticky=NSEW)

root.mainloop()