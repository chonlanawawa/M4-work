import pandas as pd

df = pd.read_excel("Stock.xlsx")
df_edit = df

#เมนูค้นหาสินค้า
def inoutfunc(search):
 df = pd.read_excel("Stock.xlsx")
 inout = input("ต้องการนำเข้าสินค้าหรือนำออกสินค้า (พิมพ์ นำเข้า / นำออก):")
 inout_amount = int(input("ต้องการนำเข้าหรือนำออกสินค้าเป็นจำนวนเท่าไหร่:"))
 if inout == "นำเข้า":
    print("นำเข้าสินค้าเป็นจำนวน",int(inout_amount),"ชิ้น")
    save_inout = (input("ต้องการบันทึกข้อมูลหรือไม่ (ใช่ / ไม่):"))
    amt = int(df.Amount[df.Name==search])
    changed_amt = amt+inout_amount
    if save_inout == "ใช่":
        df_edit.replace(to_replace=amt,value=changed_amt,inplace=True)
        print("ทำรายการสำเร็จ")
        mainfunc()
    elif save_inout == "ไม่":
        print("ทำรายการสำเร็จ")
        mainfunc()
    else:
        print("กรุณาลองอีกครั้ง")
        inoutfunc(search)
 elif inout == "นำออก":
    print("นำออกสินค้าเป็นจำนวน",int(inout_amount),"ชิ้น")
    save_inout = (input("ต้องการบันทึกข้อมูลหรือไม่ (ใช่ / ไม่):"))
    amt = int(df.Amount[df.Name==search])
    changed_amt = amt-inout_amount
    if save_inout == "ใช่":
        df_edit.replace(to_replace=amt,value=changed_amt,inplace=True)
        print("ทำรายการสำเร็จ")
        mainfunc()
    elif save_inout == "ไม่":
        print("ทำรายการสำเร็จ")
        mainfunc()
    else:
        print("กรุณาลองอีกครั้ง")
        inoutfunc(search)
 else:
    print("กรุณาลองอีกครั้ง")
    inoutfunc() 

def searchfunc(df_edit):
    print("เมนูค้นหาสินค้า")
    search = input("กรุณาระบุชื่อสินค้า:")
    datamatch = list(df_edit.Name.str.match(search))
    if datamatch.__contains__(True):
        print("พบสินค้า",search)
        inoutfunc(search)
    else:
        print("ไม่พบสินค้า กรุณาลองอีกครั้ง")
        searchfunc(df_edit)

#เมนูเพิ่มสินค้า
def addfunc():
    global df_edit
    print("เมนูเพิ่มสินค้า")
    new_name = input("ระบุชื่อสินค้า:")
    new_category = input("ระบุประเภทของสินค้า:")
    new_price = input("ระบุราคาสินค้า:")
    new_amount = input("ระบุจำนวนสินค้าที่นำเข้า:")
    save_add = input("ต้องการบันทึกรายการหรือไม่ (ใช่ / ไม่):")
    new_product = [[new_name,new_category,new_price,new_amount]]
    cols = ["Name","Category","Price","Amount"]
    if save_add == "ใช่":
        df_edit.set_index("Name",inplace=True)
        new_row = pd.DataFrame(data=new_product,columns=cols)
        new_row.set_index("Name",inplace=True)
        df_edit = df_edit.append(new_row)
        df_edit.reset_index(inplace=True)
        print("ทำรายการสำเร็จ")
        mainfunc()
    elif save_add == "ไม่":
        print("ทำรายการสำเร็จ")
        mainfunc()
    else:
        print("กรุณาลองอีกครั้ง")
        addfunc()

#เมนูลบสินค้า
def delfunc(df,df_edit):
    df = pd.read_excel("Stock.xlsx")
    print("เมนูลบสินค้า")
    search_del = input("กรุณาระบุชื่อสินค้าที่ต้องการจะลบ:")
    match_del = list(df.Name.str.match(search_del))
    if match_del.__contains__(True):
        print("พบสินค้า\t",search_del)
        save_del = input("ต้องการบันทึกการลบหรือไม่ (ใช่ / ไม่):")
        if save_del == "ใช่":
            index = df_edit[df_edit.Name.str.match(search_del)].index
            df_edit.drop(index,axis=0,inplace=True)
            print("ทำรายการเสร็จสิ้น")
            mainfunc()
        elif save_del == "ไม่":
            print("ทำรายการเสร็จสิ้น")
            mainfunc()
        else:
            print("กรุณาลองอีกครั้ง")
            delfunc(df,df_edit)
    else:
        print("ไม่พบสินค้า กรุณาลองอีกครั้ง")
        delfunc(df,df_edit)

def endfunc(df_edit):
    print("สิ้นสุดการทำงานและบันทึกไฟล์")
    df_edit.set_index("Name",inplace=True)
    df_edit.to_excel("Stock(edited).xlsx")
    print("บันทึกไฟล์สำเร็จ")

def mainfunc():
    print("โปรแกรมจัดการร้านค้า")
    choose = int(input("พิมพ์ตัวเลขเพื่อเลือกเมนูการใช้งาน\n1 สำหรับเมนูค้นหาสินค้า\n2 สำหรับเมนูเพิ่มสินค้า\n3 สำหรับเมนูลบสินค้า\n4 สำหรับการสิ้นสุดการทำงานและบันทึกไฟล์\n"))
    if choose == 1:
        searchfunc(df_edit)
    elif choose == 2:
        addfunc()
    elif choose == 3:
        delfunc(df,df_edit)
    elif choose == 4:
        endfunc(df_edit)
    else:
        print("กรุณาลองอีกครั้ง")
        mainfunc()

mainfunc()