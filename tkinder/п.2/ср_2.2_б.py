from tkinter import *
root=Tk()
root.title('Узор_2')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
def inter(A,B,q):
    (xa,ya)=A
    (xb,yb)=B
    return (xa+q*(xb-xa), ya+q*(yb-ya))

L=[(20,180),(180, 180),(100,10)]
q=0.1; n=15
for i in range(n):
    canvas.create_line(L,L[0],fill='blue')
    L=[inter(L[i],L[(i+1)%3],q) for i in range(3)]
