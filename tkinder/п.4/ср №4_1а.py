from geom_sys import *
from tkinter import *
root=Tk()
root.title('тунель')
canvas=Canvas(root,width=240,height=240,bg='white')
canvas.pack()

# задаём параметры узора
(xa,ya)=(185,140); # точка выхода лучей
(xs,ys)=(120,120); R=90; # центр и радиус круга
n=60; u0=0; du=360
# рисуем узор
canvas.create_oval(xs-R,ys-R,xs+R,ys+R)
for k in range(n+1):
    fi=u0+k/n*du
    (x,y)=ps2ds((xs,ys),(R,fi))
    canvas.create_line(xa,ya,x,y)
    canvas.create_oval(x-5,y-5,x+5,y+5,fill='white')
canvas.create_oval(xa-35,ya+20,xa+15,ya-30,
                   fill='white',outline='white')
