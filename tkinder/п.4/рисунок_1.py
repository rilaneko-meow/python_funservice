from geom_sys import *
from tkinter import *
root=Tk()
root.title('Рисунок_1')
canvas=Canvas(root,width=250,height=250,bg='white')
canvas.pack()

(sx,sy)=(120,120)
for k in range(4):
    for R in range(10,91,5):
        canvas.create_arc(sx-R,sy-R,sx+R,sy+R,
                          start=k*90-R/2,extent=R,style='arc')
