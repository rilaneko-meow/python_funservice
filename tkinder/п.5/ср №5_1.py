from geom_sys import *
from tkinter import *
root=Tk()
root.title('Калейдоскоп')
canvas=Canvas(root,width=300,height=200,bg='white')
canvas.pack()

A=(55,178)
B=(145,178)
C=(100,100)


L1=[(88,130),(100,150),(124,152),(112,140),(100,106)]
L2=[(70,152),(136,166),(98,176)]


P=C; Q=B; R=A
for k in range(6):
    canvas.create_polygon(P,Q,R,fill='orange',
                          width=1,outline='black')
    canvas.create_polygon(L1,fill='pink')
    canvas.create_polygon(L2,fill='brown')
    R=symmetry(P,Q,R)
    L1=symmetry(P,Q,L1)
    L2=symmetry(P,Q,L2)
    Q,R=R,Q

