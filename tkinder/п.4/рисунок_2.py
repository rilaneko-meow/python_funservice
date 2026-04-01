from geom_sys import *
from tkinter import *
root=Tk()
root.title('Рисунок_2')
canvas=Canvas(root,width=250,height=250,bg='white')
canvas.pack()

(sx,sy)=(120,120)
for k in range(3):
    for R in range(10,91,5):
        canvas.create_arc(sx-R,sy-R,sx+R,sy+R,
                          start=k*120-R,style='arc')
