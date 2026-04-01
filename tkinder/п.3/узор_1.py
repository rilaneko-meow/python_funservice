from tkinter import *
from math import *
root=Tk()
root.title('Узор_1')
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

# задаём параметры многоугольника
n=13; R1=30; R2=80; df=360/n
# задаём начало координат
S = (100,100)
V = [(R1,90-df),(R2,90),(R1,90+df)]
for i in range(n):
    pts = ps2ds(S,V)
    canvas.create_line(pts)
    V = [(R,fi+df) for (R,fi) in V]
