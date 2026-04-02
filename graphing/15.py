import math

from graph import *

t = int(input())

rectangle(10, 10, 100, 210)

for i in range(math.floor(200/math.floor(200 / (t+1)))):
    line(10, 10 + i * math.floor(200 / (t+1)), 100, 10+ i* math.floor(200 / (t+1)))

run()