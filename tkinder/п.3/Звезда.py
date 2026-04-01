from tkinter import *
from math import *
root=Tk()
root.title('Звезда')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

# функция перехода к декартовым координатам
"""
     S - центр системы координат
     L - точка (кортеж) или список точек (кортежей)
     в полярной системе координат с центром в точке S
     результат - точка (кортеж) или список точек (кортежей)
     в экранной системе координат
"""
def ps2ds(S,L):
    (xs,ys)=S
    if type(L) == tuple:
        (R,fi)=L
        return (xs + R*cos(pi*fi/180),
                ys - R*sin(pi*fi/180))
    if type(L) == list:
        return [(xs + R*cos(pi*fi/180),
                ys - R*sin(pi*fi/180)) for (R,fi) in L]

# задаём параметры рисунка
n=5; k=2; R=80
# задаём начало координат
(xs,ys)= S = (100,105)
# задаём полярный угол «нулевой» вершины звезды
fi = 90
# задаём приращение угла
df = 360/n
# вычисляем полярные координаты всех вершин
V = [(R,fi+i*df) for i in range(n)]
# переводим их в экранные координаты
pts = ps2ds(S,V)
# рисуем звездчатый многоугольник
for i in range(n):
 j=(i+k)%n
 canvas.create_line(pts[i],pts[j],width=2)
