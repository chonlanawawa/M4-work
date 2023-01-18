import pandas as pd

df = pd.read_excel("Stock.xlsx",index_col="Name") #เอาคอลัมที่กำหนดมาแทนindexที่เป็นเลข

#การเรียงข้อมูลด้วย index
# result = df.sort_index() #เรียงตามลำดับพยัญชนะ
# print(result)
# result2 = df.sort_index(ascending=False) #เรียงตามลำดับพยัญชนะแบบกลับหลัง
# print(result2)

#เรียงข้อมูลด้วยvalue
#result3 = df.sort_values("Price")
#print(result3)

#การเพิ่มคอลัมน์
# df["delivery"]=100
# df["total"]= df["Price"]+df["delivery"] #เอาค่าในคอลัมมารวมกันได้/sum
# print(df)

#การลบคอลัมน์
#result=df.drop("Amount",axis=1,inplace=True) #inplace=แบบบันทึกลงdf
#print(result)

#การเปลี่ยนชื่อคอลัมน์
#cols={"Amount":"Number"}
#df.rename(columns=cols,inplace=True)
#print(df)

#การเพิ่มแถว
# products = [["หูฟัง",1500,"อุปกรณ์คอมพิวเตอร์"],["สายชาร์จ",500,"อุปกรณ์คอมพิวเตอร์"]]
# cols = ["Name","Price","Category"]
# newdf = pd.DataFrame(data=products,columns=cols)
# newdf.set_index("Name",inplace=True)
# df = df.append(newdf)
# print(df)

#การลบแถวด้วยindexตัวเลข
# df = pd.read_excel("Stock.xlsx")
# rows = [3,9,10]
# df.drop(rows,axis=0,inplace=True) #ลบแถวที่3 9 10
# print(df)

#การลบแถวด้วยindexข้อความ
# rows=["ยางลบ","รถบังคับ"]
# df.drop(rows,axis=0,inplace=True)
# print(df)

#การลบข้อมูลที่ซ้ำ
df[df.duplicated()]
print(df)