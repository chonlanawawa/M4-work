from scipy.io import loadmat
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt

mnist_raw = loadmat("mnist-original.mat")

mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}

x,y=mnist["data"],mnist["target"]

x_train,x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]

#a
def score_a():
    k_neighbors=np.arange(1,11) #best=3
    train_score=np.empty(len(k_neighbors))
    test_score=np.empty(len(k_neighbors))
    for i,k in enumerate(k_neighbors):
     knn=KNeighborsClassifier(n_neighbors=k)
     knn.fit(x_train,y_train)
     train_score[i]=knn.score(x_train,y_train)
     test_score[i]=knn.score(x_test,y_test)
    plt.title("Compare k value in model")
    plt.plot(k_neighbors,test_score,label="Test_score")
    plt.plot(k_neighbors,train_score,label="Train_score")
    plt.legend()
    plt.xlabel("k Number")
    plt.ylabel("Score")
    plt.show()
# score_a()
    
knn=KNeighborsClassifier(n_neighbors=3) 
knn.fit(x_train,y_train)

#b
print("\nb")
y_pred=knn.predict(x_test)
print(classification_report(y_test,y_pred))
print("จำนวน x",len(x_test))
print("จำนวน y",len(y_test))
print("ความแม่นยำ = ",accuracy_score(y_test,y_pred)*100)

#c
print("\nc")
print(confusion_matrix(y_test,y_pred))
print(pd.crosstab(y_test,y_pred,rownames=["Actually"],colnames=["Prediction"],margins=True))

#d
print("\nd")
num1=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,116,243,224,246,59,0,31,121,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,149,191,95,8,158,25,17,219,228,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,173,149,56,0,0,61,5,198,228,44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,86,200,25,0,0,0,0,66,203,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,138,0,0,0,0,43,243,230,46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,139,201,6,0,0,0,0,149,252,84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,88,228,10,0,0,0,18,152,253,139,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,225,96,0,0,2,68,194,224,110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,49,229,20,28,60,151,255,249,71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,249,206,253,221,206,246,202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,106,196,123,16,135,246,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,254,198,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,29,250,237,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,219,210,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,112,244,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,244,124,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94,233,164,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,211,222,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,211,125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,90,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).reshape(1,-1)
num2=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,255,255,191,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,255,191,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,255,255,128,64,0,64,255,255,255,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,191,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,128,255,255,255,255,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,255,255,255,255,255,255,255,191,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,191,255,255,255,255,255,255,255,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,255,255,255,255,128,255,255,255,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,191,255,255,255,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,255,255,255,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,255,255,255,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,0,0,0,0,0,0,0,128,255,255,255,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,255,255,191,64,0,0,64,64,191,255,255,191,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,191,255,255,255,255,255,255,255,255,255,255,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,128,191,255,255,255,255,255,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).reshape(1,-1)
num1_pred = knn.predict(num1)
num2_pred = knn.predict(num2)
print("num1 =",num1_pred)
print("num2 =",num2_pred)




