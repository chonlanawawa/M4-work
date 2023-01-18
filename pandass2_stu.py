import pandas as pd

df = pd.read_excel("stu_score.xlsx")
#df = df.Gender.astype("category") #เรียกมาคอลัมนึงแล้วจัดเป็นcategory
#print(df)
 
#print(df[:]) #เอาทั้งหมด
#print(df[1:4]) #แถว1-3
#print(df[1:4].Age) #แค่age แถว1-3

#เลือกคอลัมปกติใช้แค่ .ชื่อคอลัม แต่ถ้าอยากได้เป็นช่วง-หลายตัว
#Sscore = df.Score[1:3] #ช่วงแบบคอลัมเดียว
#print(Sscore)
#Sscore = df[["Grade","Score"]][1:3] #แบบหลายคอลัม
#print(Sscore)

# Gmatch=df[df.Name.str.match("L")] #นับจากตัวแรก
# print(Gmatch)
# Gcontains=df[df.Gender.str.contains("m")] #อยู่ตัวไหนก็ได้
# print(Gcontains)

#MatchA=df[df.Grade.str.match("A")]
#print(MatchA[["Name","Grade"]])

#เลือกแถวแบบวนรอบ
#for idx,row in df.iterrows(): 
    #print(idx,row) #คอลัมมาจับคู่กับแถวแล้วเรียงไปเรื่อยๆ เป็น categoryคู่ข้อมูล
    #print("Name : {}\t|Age : {}".format(row.Name,row.Age))
    # print(f"Name : {row.Name:10} |Age : {row.Age}")  #แบบนี้จองพื้นที่ได้ ไม่ต้องใช้แท้บ
    # print("Name :",row.Name,"\t|Age :",row.Age)

#แบบมีเงื่อนไข เอาข้อมูลต้องมีก้ามปูด้วย
# ss = df[df.Score<60]
# print(ss)
# ss = df[(df.Gender=="Female")&(df.Grade == "A")] #และ
# print(ss)
#ss = df[(df.Gender=="Female") | (df.Grade == "A")] #หรือ
#print(ss)

#isinใช้แทนorกรณีเกิน2เงื่อนไข
ss = df[(df.Score.isin([50,60,70]))]
print(ss)
ss2 = df[(df.Grade.isin(["A","B","C"]))]
print(ss2)