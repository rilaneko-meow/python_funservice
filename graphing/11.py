from graph import *

def rect_col(x,y,co,c):
    brushColor(c)

    for i in range(co):
        polygon([
            (x,y),
            (x+25,y+25),
            (x,y+50),
            (x-25,y+25),
            (x,y)
        ])
        y+=50

for i in range(int(input())):
    rect_col(25+i*50,0,10,'cyan')
run()