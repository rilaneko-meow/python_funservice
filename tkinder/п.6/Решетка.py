from geom_sys import *
from tkinter import *
root=Tk()
root.title('Решетка')
canvas=Canvas(root,width=240,height=200,bg='white')
canvas.pack()
S =(50,75)
V1=(40,-10)
V2=(10, 40)
for i in range(3):
    for j in range(4):
        w=add(S,mlt(V1,j),mlt(V2,i))
        create_circle(canvas,w,20,fill='gray')
