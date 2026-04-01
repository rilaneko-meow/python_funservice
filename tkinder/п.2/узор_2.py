from tkinter import *
root=Tk()
root.title('Узор')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

def partition(A,B,n):
    (xa,ya)=A
    (xb,yb)=B
    dx=(xb-xa)/n
    dy=(yb-ya)/n
    return [(xa+i*dx, ya+i*dy) for i in range(n+1)]

A=(30, 80)
B=(180, 30)
C=(160,170)
D=(60,170)
canvas.create_text(A,text='A', anchor=SE)
canvas.create_text(B,text='B', anchor=SW)
canvas.create_text(C,text='C', anchor=NW)
canvas.create_text(D,text='D', anchor=NE)
S=(120,120)
n=6
AS=partition(A,S,n)
BS=partition(B,S,n)
CS=partition(C,S,n)
DS=partition(D,S,n)
for L in zip(AS,BS,CS,DS):
    canvas.create_polygon(L,outline='black',fill='')
