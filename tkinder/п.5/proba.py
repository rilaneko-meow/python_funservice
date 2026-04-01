from geom_sys import *
from tkinter import *
root=Tk()
root.title('Калейдоскоп')
canvas=Canvas(root,width=300,height=200,bg='white')
canvas.pack()

A=(65,178)
B=(116,178)
C=(87,100)


L1=[(88,130),(100,150),(124,152),(112,140),(100,106)]
#L2=[(80,152),(116,156),(70,176)]
#L3=[(110,176),(100,166),(140,170),(130,166),(124,145)]


P=C; Q=B; R=A
for k in range(10):
    canvas.create_polygon(P,Q,R,fill='orange',
                          width=1,outline='black')
    canvas.create_polygon(L1,fill='pink')
#    canvas.create_polygon(L2,fill='brown')
#    canvas.create_polygon(L3,fill='purple')
    R=symmetry(P,Q,R)
#    L1=symmetry(P,Q,L1)
#    L2=symmetry(P,Q,L2)
#    L3=symmetry(P,Q,L3)
    Q,R=R,Q

