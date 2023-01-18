import numpy as np
import matplotlib.pyplot as plt

#ทางจักรยานทั้งหมดในเขตกรุงเทพมหานคร ณ เดือนมิถุนายน ปี2558
distance = [24.00,21.00,20.40,16.00,15.60,14.00,12.88,10.20,10.00,9.00,8.00,8.00,8.00,8.00,4.80,4.50,4.40,4.00,3.80,3.50,3.20,3.00,3.00,2.80,1.66,1.30,1.30,1.00,1.00,0.50]
name = ['ถนนประดิษฐ์มนูญธรรม','ถนนลาดพร้าว','ถนนพหลโยธิน','ถนนเพชรเกษม','ถนนรามคำแหง','ถนนจรัญสนิทวงศ์-รัชดาภิเษก','ชมกรุงรอบเกาะรัตนโกสินทร์ ระยะ 1 + ระยะ 2','ถนนสุขาภิบาล 5 (สายไหม)','ถนนราษฎร์บูรณะ','ถนนนราธิวาสราชนครินทร์','ถนนเจริญนคร','ถนนสมเด็จพระเจ้าตากสิน','ถนนพุทธมณฑล สาย2','โครงการปรับปรุงบางขุนเทียนชายทะเล ระยะ2','ถนนกรุงธนบุรี','ซอยวัดอินทราวาส','โครงการปรับปรุงภูมิทัศน์พระบรมราชานุสาวรีย์สมเด็จพระเจ้าตากสินมหาราช','ถนนสรงประภา','ถนนอุทยาน','โครงการปรับปรุงบางขุนเทียนชายทะเล ระยะ1','ถนนราชดำริ','ถนนสุขุมวิท','ถนนสะแกงาม','ถนนสาทร (เหนือ-ใต้)','ถนนอรุณอัมรินทร์ตัดใหม่','ทางเดินเลียบคลองไผ่สิงห์โต','ถนนประชาชื่น','ถนนพุทธมณฑลสาย 3','ถนนดวงพิทักษ์','โครงการปรับปรุงสะพานเลียบคลอง ค.ส.ล.จากถนนพระยามนธาตุราชศรีพิจิตร์']

typelist = ['ทางจักรยานเฉพาะ','ร่วมบนทางเท้า','บนทางเท้าร่วมกับผิวจราจร','บนไหล่ทาง','บนผิวจราจร']
typeeng = ['Specific bike lane','On sidewalk','On sidewalk and road surface','On shoulder','On road surface']
distype = [[24.00,4.00,3.80,1.30,1.00,1.00],[21.00,20.40,16.00,15.60,14.00,10.20,10.00,9.00,8.00,8.00,8.00,4.80,4.50,3.50,3.20,3.00,3.00,1.66,1.30],[12.88],[8.00,0.50],[4.40,2.80]]
sum_dis = [sum(distype[0]),sum(distype[1]),sum(distype[2]),sum(distype[3]),sum(distype[4])]

sum_array = np.array(sum_dis)
type_array = np.array(typeeng)
dis_array = np.array(distype)

print("ผลรวมระยะทางของทางจักรยานแต่ละประเภท (กิโลเมตร)",sum_array)

print("sum =",np.sum(dis_array[0]),np.sum(dis_array[1]),np.sum(dis_array[2]),np.sum(dis_array[3]),np.sum(dis_array[4]))
print("mean =",np.mean(dis_array[0]),np.mean(dis_array[1]),np.mean(dis_array[2]),np.mean(dis_array[3]),np.mean(dis_array[4]))
print("min =",np.min(dis_array[0]),np.min(dis_array[1]),np.min(dis_array[2]),np.min(dis_array[3]),np.min(dis_array[4]))
print("max =",np.max(dis_array[0]),np.max(dis_array[1]),np.max(dis_array[2]),np.max(dis_array[3]),np.max(dis_array[4]))

color = ['red','orange','cyan','yellow','green']
protitle = {"size":14,"color":"black","backgroundcolor":"yellow"}

plt.pie(sum_dis,labels=typeeng,autopct='%.1f%%',colors=color)
plt.title("Proportion of each type of bicycle lane in Bangkok (June 2015)",protitle,loc="center")
plt.legend(typeeng,loc=0,title="Type of bicycle lane",title_fontsize="large",fontsize="large",facecolor="pink",edgecolor="black")
plt.show()
