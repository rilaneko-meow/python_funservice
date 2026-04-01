from geom_sys import *
from tkinter import *
root=Tk()
root.title('Паркет_7')
canvas=Canvas(root,width=450,height=180,bg='white')
canvas.pack()

def elem(S,q):
    # 0 1 2 3 4 5 6 - номер точки
    SH=[(0,1),(2,0),(4,1),(2,2),(0,2),(2,3),(4,2)]
    # масштабирование и перенос шаблона
    L=move(S,mlt(SH,q))
    up=[L[k] for k in (0,1,2,3)]
    lf=[L[k] for k in (0,3,5,4)]
    rt=[L[k] for k in (2,3,5,6)]
    canvas.create_polygon(up,outline='black',
                          fill='lightgray')
    canvas.create_polygon(lf,outline='black',
                          fill='white')
    canvas.create_polygon(rt,outline='black',
                          fill='gray')
# ------------ main -----------
S=(20,20); q=20
V1=(4*q,0)
V2=(2*q,2*q)
n=3; m=4
# рисуем двумерный узор
for i in range(n):
    for j in range(m):
        w=add(S,mlt(V1,j),mlt(V2,i))
        elem(w,q)

