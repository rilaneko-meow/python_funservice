from graph import *

def draw_triang(x,y,c):
    brushColor(c)

    polygon([(x,y),(x+30,y+40),(x+60,y),(x,y)])

draw_triang(0,0,'red')
draw_triang(60,0,'green')
draw_triang(30,40,'blue')

run()