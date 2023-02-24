from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("diabetes.csv")
print(df.head())
print(df.shape)

x=df.drop("Outcome",axis=1).values
y=df["Outcome"].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)

k_neighbors=np.arange(1,20) #3 the best
train_score=np.empty(len(k_neighbors))
test_score=np.empty(len(k_neighbors))

for i,k in enumerate(k_neighbors):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    train_score[i]=knn.score(x_train,y_train)
    test_score[i]=knn.score(x_test,y_test)
    # print(test_score[i])

plt.title("Compare k value in model")
plt.plot(k_neighbors,test_score,label="Test_score")
plt.plot(k_neighbors,train_score,label="Train_score")
plt.legend()
plt.xlabel("k Number")
plt.ylabel("Score")
plt.show()

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test) #เอาข้อมูลจากข้างนอกมาจัดเป็นarrayแล้วpredictเลยได้
print(pd.crosstab(y_test,y_pred,rownames=["Actually"],colnames=["Prediction"],margins=True))