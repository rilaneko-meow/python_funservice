from geom_sys import *
from tkinter import *
root=Tk()
root.title('Сектор_1')
canvas=Canvas(root,width=240,height=240,bg='white')
canvas.pack()

def sector(obj, A, S, R, n, u0, du, cv, w=1):
    (xa,ya)=A; (xs,ys)=S
    obj.create_arc(xs-R,ys-R,xs+R,ys+R,
                   start=u0,extent=du,style=ARC,
                   outline=cv,width=w)
    for k in range(n+1):
        fi=u0+k/n*du
        (x,y)=ps2ds(S,(R,fi))
        obj.create_line(A,(x,y),fill=cv,width=w)

sector(canvas, A=(100,100), S=(150,100),
       R=70, n=6, u0=-60, du=120, cv='brown',w=3)
