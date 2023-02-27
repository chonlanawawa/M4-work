import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-5,5,10) #จำลองข้อมูลตั้งแต่ -5 ถึง 5 จำนวน10ตัว
# y = 2*x+1
# plt.scatter(x,y,color="red",label="y=2x+1")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend(loc="upper left")
# plt.title("Graph y=2x+1")
# plt.grid()
# plt.show()

rng = np.random
x = rng.rand(50)*10
y = 2*x+rng.randn(50)
print(x)
print(y)
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()