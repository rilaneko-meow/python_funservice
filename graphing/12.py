from graph import *

def romb(x,y):
    polygon([
        (x,y),
        (x+25,y+25),
        (x,y+50),
        (x-25,y+25),
        (x,y)
    ])

def frac(x,y,c):
    brushColor(c)
    romb(x-50,y)
    romb(x,y)
    romb(x+50,y)
    romb(x,y-50)
    romb(x,y+50)


for i in range(int(input())):
    frac(100+i*150,100,'cyan')

run()