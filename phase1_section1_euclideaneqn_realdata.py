import matplotlib.pyplot as plt
import random

length = int(input('Enter the no. of nodes u want : '))
k = random.uniform(0.0, 5.0)
x1 = []
y1 = []
x2 = []
y2 = []

for i in range(0, length):
    x1.append(random.uniform(0.0, 1.5))
    y1.append(random.uniform(0.0, 1.5))
    x2.append(random.uniform(3.5, 5.0))
    y2.append(random.uniform(3.5, 5.0))

test_dist = []

for j in range(0, length):
    test_dist.append(((x1 - x2)**2) + ((y1 - y2)**2))