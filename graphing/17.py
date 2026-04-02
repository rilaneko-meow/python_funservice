import math

from graph import *

t = int(input())

for i in range(t+1):
    line(10 + i * math.floor(200 / (t+1)), 10, 60+ i* math.floor(100 / (t+1)), 100)

line(10, 10,10+ t*math.floor(200 / (t+1)),10)
line(60, 100,60+ t*math.floor(100 / (t+1)),100)
run()
