from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,accuracy_score

iris_dataset=load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris_dataset["data"],iris_dataset["target"],test_size=0.4,random_state=0)

knn=KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train,y_train)

pred_number=2
pred=knn.predict([x_test[pred_number]])

print("target = ",y_test[pred_number])
print("ผลการพยากรณ์",pred)
print("ทำนายว่าอยู่กลุ่มสายพันธ์ุ",iris_dataset["target_names"][pred])

y_pred=knn.predict(x_test)
print(classification_report(y_test,y_pred))
print(classification_report(y_test,y_pred,target_names=iris_dataset["target_names"]))
print("ความแม่นยำ = ",accuracy_score(y_test,y_pred)*100)