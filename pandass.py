import pandas as pd
import numpy as np

#data_ls = [10,20,"computer",15.05,"orange"]
#data_tp = (10,20,"com",15.05,"brown")
#ndata = np.array(data_ls)
#ps1=pd.Series(data_ls)
#ps2=pd.Series(data_tp)
#ps3=pd.Series(ndata)
#print(ps1)
#print(ps2)
#print(ps3)

#a = [1,7,2]
#myvar = pd.Series(a, index=["x","y","z"]) #กำหนดindex
#print(myvar)

#ใช้ dictionary จะกำหนด indexได้เลย key=index ส่วน value=elements value
#calories = {"day1":420,"day2":380,"day3":390}
#myvar = pd.Series(calories)
#print(myvar[:])

#print(myvar["day1"]) #ใช้keyแทนindexได้เลย
#print(myvar[1])

#data  = ["orange","mango","grape","lemon"]
#cols = ["Fruit"]
#data_ps = pd.DataFrame(data,columns = cols) #กำหนดcolumnให้pd ถ้าไม่กำหนดชื่อcolsจะเป็น 0 
#print(data_ps)

#ใช้dictสร้างได้ key=ชื่อคอลัมน์ value=ค่า
#data = {"calories":[420,380,390],"duration":[50,40,45]}
#df = pd.DataFrame(data)
#print(df)

data_Fruit = ["orange","mango","grape","lemon"]
data_color = ["orange","green","purple","green"]
data_num = [50,10,50,60]

#zip รวมlistหลายๆอัน
#data = list(zip(data_Fruit,data_color,data_num))
#cols = ["Fruit","color","number"]
#data_ps = pd.DataFrame(data,columns = cols)
#print(data_ps)

#ทำเป็นseriesหลายๆอันละค่อยรวมเป็น dataframe
#F = pd.Series(data_Fruit)
#C = pd.Series(data_color)
#N = pd.Series(data_num)
#frame = {"Fruit":F,"Color":C,"Number":N}
#data_ps = pd.DataFrame(frame) 
#data_ps.to_csv("product.csv") #ทำเป็นfile csv เปิดปกติเจอเป็นคอมม่าคั่น ในเอ็กเซลเป็นตาราง
#print(data_ps)

#อ่านไฟล์csv
#data_csv = pd.read_csv("product.csv",encoding="utf-8")
#cols = ["Fruit","Number"] 
#data_product = pd.read_csv("product.csv",usecols=cols,index_col="Fruit") #เลือกได้ว่าจะใช้คอลัมน์ไหนบ้างด้วยusecols
#print(data_product)


