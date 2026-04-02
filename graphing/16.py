import math

from graph import *

t = int(input())

for i in range(math.floor(200/math.floor(200 / (t+1)))):
    line(10, 10 + i * math.floor(200 / (t+1)), 200, 200 - (i* math.floor(200 / (t+1))))

run()