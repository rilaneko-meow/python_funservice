from graph import *

def rect(x,y,c1,c2):
    brushColor(c1)
    polygon([
        (x,y),
        (x-20,y-20),
        (x+20,y-20),
        (x,y),
    ])
    polygon([
        (x,y),
        (x-20,y+20),
        (x+20,y+20),
        (x,y),
    ])
    brushColor(c2)
    polygon([
        (x,y),
        (x+20,y+20),
        (x+20,y-20),
        (x,y),
    ])
    polygon([
        (x,y),
        (x-20,y+20),
        (x-20,y-20),
        (x,y),
    ])

def draw_col(x,y,var):
    c1 = 'cyan'
    c2 = 'white'
    if var:
        c1 = 'white'
        c2 = 'cyan'
    rect(x,y,c1,c2)
    rect(x,y+40,c2,c1)

for i in range(8):
    draw_col(40+i*40,40,i%2)

run()