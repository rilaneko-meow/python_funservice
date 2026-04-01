from geom_sys import *
from tkinter import *
root=Tk()
root.title('ср №6_3')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()
# ----------------------------------------
def elem(S,q):
    # шаблон элемента
    SH=[(0.75,0.75),(-0.75,0.75),(-0.75,-0.75),(0.75,-0.75)]
    # масштабирование и перенос шаблона
    L=move(S,mlt(SH,q))
    # рисование элемента узора
    canvas.create_polygon(L,width=1,outline='red',
                          fill='orange')
# ----------- main -----------
# параметры узора:
S=(40,40); q=20; n=3; m=5
# S – центр первого квадрата
# q – коэффициент масштабирования
# n, m – количество рядов и столбцов паркета
# формирование векторов сдвига
V1=(q*2,0)
V2=(0,q*2)
# вложенный цикл рисования паркета
for i in range(n):
    for j in range(m):
        w=add(S,mlt(V1,j),mlt(V2,i))
        elem(w,q)

