import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

length = int(input('Enter the no. of sections u want:'))
section1 = []
section2 = []
num1 = []
num2 = []

for j in range(length):
    num1.append(random.uniform(0.0, 1.5))
    num2.append(random.uniform(3.5, 5.0))
    
for i in range(0, length):
    section1.append(random.randint(0, 1))
    section2.append(random.randint(4, 5))
    
# Scatter plot
for i in range(0, length):
    plt.scatter(section1[i], section2[i])

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Basic Scatter Plot")

# Show plot
plt.show()