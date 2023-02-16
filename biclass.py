from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score
import itertools
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

mnist_raw = loadmat("mnist-original.mat")
mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}

x,y=mnist["data"],mnist["target"]

x_train,x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]

predict_number =  9999
y_train_7 = (y_train==9)
y_test_7 = (y_test==9)

def displayImage(x):
    plt.imshow(
    x.reshape(28,28),
    cmap=plt.cm.binary,
    interpolation="nearest"
    )
    plt.show()

def displayPredict(clf,actually_y,x):
    print("Actually =",actually_y)
    hh = clf.predict([x])[0]
    print("Prediction =",hh)
    return hh
    

sgd_clf = SGDClassifier()
sgd_clf.fit(x_train,y_train_7)

displayPredict(sgd_clf,y_test_7[predict_number],x_test[predict_number])

#find prediction = false
# for i in range(7700,10000):
#     predict_number =  i
#     y_train_7 = (y_train==7)
#     y_test_7 = (y_test==7)
#     hh = displayPredict(sgd_clf,y_test_7[predict_number],x_test[predict_number])
#     displayPredict(sgd_clf,y_test_7[predict_number],x_test[predict_number])
#     print(predict_number)
#     if hh  == False:
#         displayImage(x_test[predict_number])
#         break

score = cross_val_score(sgd_clf, x_train, y_train_7, cv = 3, scoring = 'accuracy')
print(score)

y_train_pred = cross_val_predict(sgd_clf,x_train,y_train_7,cv=3)
cm = confusion_matrix(y_train_7,y_train_pred)
print(cm)

y_test_pred = sgd_clf.predict(x_test)

# classes = ["Other Number","Number 9"]
# print(classification_report(y_test_7,y_test_pred,target_names=classes))

print("accuracy Score =",accuracy_score(y_test_7,y_test_pred)*100)
displayImage(x_test[predict_number])
