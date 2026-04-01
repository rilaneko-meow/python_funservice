from tkinter import *
root=Tk()
root.title('Узор_3')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

def inter(A,B,q):
    (xa,ya)=A
    (xb,yb)=B
    return (xa+q*(xb-xa), ya+q*(yb-ya))

L=[(100,60),(60, 90),(60,120),(100,150),(140,120),(140,90)]
q=0.2; n=10
for i in range(n):
    canvas.create_line(L,L[0],fill='red')
    L=[inter(L[i],L[(i+1)%6],q) for i in range(6)]
