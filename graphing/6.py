from graph import *

def draw_triang(x,y,w,h,c):
    brushColor(c)

    polygon([(x-int(w/2),y),(x+int(w/2),y),(x,y-h),(x-int(w/2),y)])


draw_triang(200,140,20,60,'brown')
draw_triang(200,120,160,40,'green')
draw_triang(200,100,120,40,'green')
draw_triang(200,80,90,40,'green')
draw_triang(200,60,70,40,'green')
draw_triang(200,40,50,40,'green')

run()