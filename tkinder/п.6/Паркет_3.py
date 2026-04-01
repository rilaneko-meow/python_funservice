from geom_sys import *
from tkinter import *
root=Tk()
root.title('Паркет_3')
canvas=Canvas(root,width=280,height=200,bg='white')
canvas.pack()

def elem(S,q):
    # 0 1 2 3 4 5 - номер точки
    SH=[(0,0),(1,0),(2,1),(2,2),(1,2),(0,1)]
    # масштабирование и перенос шаблона
    L=move(S,mlt(SH,q))
    for k in range(4):
        canvas.create_polygon(L,width=3,
                              outline='black',fill='cyan')
        L = turn(S,L,90)

# ------------ main -----------
S=(60,60); q=20
V1=(4*q,0)
V2=(0,4*q)
# рисуем двумерный узор
for i in range(2):
    for j in range(3):
        w=add(S,mlt(V1,j),mlt(V2,i))
        elem(w,q)

