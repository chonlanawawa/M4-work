import matplotlib.pyplot as plt

#x = [1,2,3,4]
#y = [1,2.5,3.5,3]
#plt.bar(x,y) #bar graph
#plt.show()

#product1 = [1.2,2.8,1.3,4.3,3.5]
#product2 = [2,1.4,3.3,3.1,1.2]
#month = [1,2,3,4,5]
#plt.plot(month,product1) #กราฟเส้น
#plt.plot(month,product2)
#plt.show()

#กำหนดชื่อแกนx, y
#plt.plot([1,2,3,4],[5,6,7,8])
#plt.xlabel("X Label")
#plt.ylabel("Y Label")
#plt.show()

#บันทึกกราฟเป็นไฟล์
#plt.savefig("matplot.png")
#plt.savefig("matplot1.png",transparent=True)
#plt.show()

month = [1,2,3,4,5,]
ypoints1 = [15,30,10,20,35]
ypoints2 = [30,10,20,15,40]

#plt.plot(month,ypoints,color="m",linestyle=":",marker="v")
plt.plot(month,ypoints1,"m+--") #แบบย่อ
plt.plot(month,ypoints2,"b*--")

#plt.xlabel("month",size=20,color="red",backgroundcolor="yellow")
#plt.ylabel("price",size=20,color="blue")
data = {"size":20,"color":"red","backgroundcolor":"yellow"} #แบบกำหนดคุณสมบัติผ่านdict
plt.xlabel("Month",data)
plt.ylabel("Price",data)

#กำหนดหัวข้อ
protitle = data
plt.title("TOP PRICE",protitle,loc="center")

#legend func
plt.legend(["Mouse","Keyboard"],loc=2,title="Product",title_fontsize="xx-large",fontsize="large",facecolor="orange",edgecolor="black")

plt.show()
