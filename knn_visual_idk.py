import random
import math
import matplotlib.pyplot as plt

num1x, num1y = [], []
num2x, num2y = [], []

length = 10
k = 5

for i in range(length):
    num1x.append(random.uniform(0,1.5))
    num1y.append(random.uniform(3.5,5))

    num2x.append(random.uniform(3,5))
    num2y.append(random.uniform(0,2))

kx = random.uniform(0,5)
ky = random.uniform(0,5)

plt.scatter(num1x, num1y, color='blue', label="Category 1")
plt.scatter(num2x, num2y, color='green', label="Category 2")
plt.scatter(kx, ky, color='red', label="Test Point")

distances = []

for i in range(length):
    d1 = math.sqrt((num1x[i]-kx)**2 + (num1y[i]-ky)**2)
    distances.append((d1, "Category 1"))

    d2 = math.sqrt((num2x[i]-kx)**2 + (num2y[i]-ky)**2)
    distances.append((d2, "Category 2"))

distances.sort()

neighbors = distances[0:k]

count1 = 0
count2 = 0

for d, label in neighbors:
    if label == "Category 1":
        count1 = count1 + 1
    else:
        count2 = count2 + 1

print(f'Nearest neighbors : {neighbors}')

if count1 > count2:
    print("Prediction = Category 1")
else:
    print("Prediction = Category 2")

plt.legend()
plt.show()