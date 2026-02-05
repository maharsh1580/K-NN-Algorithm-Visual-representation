import random as r
import matplotlib.pyplot as plt
import time

section1x = []
section2x = []
section1y = []
section2y = []
num1x = []
num2x = []
num1y = []
num2y = []
x = []
y = []

f = int(input('Enter the no. of times u want to check for neighbours : '))

length = int(input('Enter the number of nodes each section must have : '))

for i in range(0, length):
    num1x.append(r.uniform(0.0, 1.5))
    num2x.append(r.uniform(0.0, 1.5))
    num1y.append(r.uniform(3.5, 5.0))
    num2y.append(r.uniform(3.5, 5.0))
    
for j in range(0, length):
    plt.scatter(num1x, num1y)
    plt.scatter(num2x, num2y)
    
kx:float = r.uniform(0.0, 5.0)
ky:float = r.uniform(0.0, 5.0)

plt.scatter(kx, ky)
    
plt.xlabel('x-axis')
plt.ylabel('y-axis')

test_dist = []
test_dist2 = []

for t in range(0, length):
    test_dist.append(((num1x[t] - kx)**2) + ((num1y[t] - ky)**2))
    test_dist2.append(((num2x[t] - kx)**2) +((num2y[t] - ky)**2))

dist1 = []
dist2 = []
test_dist.sort()
test_dist2.sort()

for q in range(0, f):
    if test_dist[q] > test_dist2[q]:
        dist1.append(test_dist2[q])
        dist2.append('Category 2')
    else:
        dist1.append(test_dist[q])
        dist2.append('Category 1')        

print(dist1)
print(dist2)

plt.show()