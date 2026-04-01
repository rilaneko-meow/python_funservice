from tkinter import *
from math import *
root=Tk()
root.title('Узор_2')
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
n=13; R1=30; R2=90
df=360/n; rd=pi*df/180
SC = 2*R1*R2*cos(rd/2)/(R1+R2)
# задаём начало координат
S = (100,100)
V = [(R1,90),(SC,90-df/2),(R2,90),(SC,90+df/2)]
for i in range(n):
    pts = ps2ds(S,V)
    canvas.create_polygon(pts,outline='black',fill='lime')
    V = [(R,fi+df) for (R,fi) in V]

