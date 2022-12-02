from tkinter import *

root = Tk()
root.title('CheckButton Test')

Label(root,text='แบบสำรวจความต้องการของตลาดแรงงาน',fg='red',bg='yellow').grid(row=0,column=0,columnspan=2,sticky=NSEW)

bool_check1 = BooleanVar()
Checkbutton(root,text='ภาษาอังกฤษ',variable=bool_check1).grid(row=1,column=0,sticky=NSEW)

value_check2 = BooleanVar()
Checkbutton(root,text='python',variable=value_check2).grid(row=1,column=1,sticky=NSEW)

show = StringVar(value='here your salt')
Label(root,textvariable=show,fg='black',bg='lightblue').grid(row=3,column=0,columnspan=2,sticky=NSEW)

def on_click():
    a = bool_check1.get()
    b = int(value_check2.get())
    show.set(f'want english {a}, want python {b}')
Button(root,text='result naja',fg='brown',command=on_click).grid(row=2,column=1,sticky=NSEW)

def reset():
    bool_check1.set(False)
    value_check2.set(False)
    show.set('here your salt')
Button(root, text='reset naja',fg='black',bg='red',command=reset).grid(row=2,column=0,sticky=NSEW)

root.mainloop()