from geom_sys import *
from tkinter import *
root=Tk()
root.title('Паркет_1')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()

# параметры узора:
S=(40,40); q=20; n=3; m=5
# S – центр первого квадрата
# q – коэффициент масштабирования

# n, m – количество рядов и столбцов паркета
# ----------------------------------------
# шаблон элемента
SH=[(1,0),(0,1),(-1,0),(0,-1)]
# масштабирование и перенос шаблона
L=move(S,mlt(SH,q))
# формирование векторов сдвига
V1=(q*2,0)
V2=(0,q*2)
# вложенный цикл рисования паркета
for i in range(n):
    LS=L
    for j in range(m):
        canvas.create_polygon(LS,width=1,outline='blue',
                              fill='cyan')
        LS=move(V1,LS)
    L=move(V2,L) 
