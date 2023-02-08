from sklearn import datasets
import matplotlib.pyplot as plt

digits_dataset = datasets.load_digits()

print(digits_dataset.target[7])
plt.imshow(digits_dataset.images[7],cmap=plt.get_cmap("gray_r"))
plt.show()
print(digits_dataset.images[7])