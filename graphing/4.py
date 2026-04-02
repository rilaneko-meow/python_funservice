from graph import *

def draw_triang(x,y,c):
    brushColor(c)

    polygon([(x,y),(x+60,y),(x,y+40),(x,y)])

draw_triang(60,0,'red')
draw_triang(60,40,'green')
draw_triang(0,40,'blue')

run()