from geom_sys import *
from tkinter import *
root=Tk()
root.title('ср №6_4')
canvas=Canvas(root,width=350,height=160,bg='white')
canvas.pack()
# ----------------------------------------
def elem(S,q):
    # шаблон элемента
    SH=[(0.5,1),(-0.5,1),(-1,0),(-0.5,-1),(0.5,-1),(1,0)]
    # масштабирование и перенос шаблона
    L=move(S,mlt(SH,q))
    # рисование элемента узора
    canvas.create_polygon(L,width=2,outline='blue',
                          fill='cyan')
# ----------- main -----------
# параметры узора:
a=40; b=40
S=(a,b); q=20; n=3; m=5
# S – центр первого квадрата
# q – коэффициент масштабирования
# n, m – количество рядов и столбцов паркета
# формирование векторов сдвига
V1=(q*2,0)
V2=(0,q*2)
# вложенный цикл рисования паркета
for i in range(n):
    a+=20
    S=(a,b)
    for j in range(m):
        w=add(S,mlt(V1,j),mlt(V2,i))
        elem(w,q)

