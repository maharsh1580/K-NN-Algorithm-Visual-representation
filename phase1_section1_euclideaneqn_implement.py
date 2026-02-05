import math
import numpy as np
import random

x1 = int(input('Enter the value of x1 : '))
y1 = int(input('Enter the value of y2 : '))

x2 = int(input('Enter the value of x2 : '))
y2 = int(input('Enter the value of y2 : '))

x_ans = x1 - x2
y_ans = y1 - y2

test_dist = x_ans**2 + y_ans**2

distance = math.sqrt(test_dist)

print(distance)