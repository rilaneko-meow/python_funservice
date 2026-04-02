from graph import *

def row(s_x,s_y, r ,co,c):
    brushColor(c)
    for i in range(co):
        circle(s_x+i*(2*r+20), s_y,r)


k = int(input())

for i in range(k):
    row(50+i*70,50+i*70,25,5,"green")
run()