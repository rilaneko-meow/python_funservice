from graph import *

def spike(x,y,lx,ly,w, c):
    brushColor(c)
    polygon([
        (x,y),
        (x+w,y),
        (lx,ly),
        (x,y)
    ])
    circle(lx,ly,10)

spike(100,200,50,75,100,'blue')
spike(150,200,300,75,100,'green')
spike(150,200,175,50,50,'red')


run()