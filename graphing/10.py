from graph import *

import math

def row(s_x,s_y, r ,co,c):
    brushColor(c)
    for i in range(math.floor(co/2)+1):
        circle(s_x-i*(2*r+20), s_y,r)
    for i in range(math.floor(co/2)+1):
        circle(s_x+i*(2*r+20), s_y,r)


k = int(input())

for i in range(k):
    row(300,50+i*70,25,i*2+1,"green")
run()