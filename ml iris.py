from sklearn import datasets

iris_dataset = datasets.load_iris()
print(iris_dataset.keys())
print(iris_dataset["DESCR"])
print(iris_dataset["target"])