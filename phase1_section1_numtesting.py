import numpy as np
import random as r
import matplotlib.pyplot as plt
import pandas as pd
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

length = int(input('Enter the number of nodes each section must have : '))

for i in range(0, length):
    num1x.append(r.uniform(0.0, 1.5))
    num2x.append(r.uniform(0.0, 1.5))
    num1y.append(r.uniform(3.5, 5.0))
    num2y.append(r.uniform(3.5, 5.0))

print(f'The values of the section1 are : x-axis : {num1x} and y-axis : {num1y}')    
print(f'The values of the section2 are : x-axis : {num2x} and y-axis : {num2y}')