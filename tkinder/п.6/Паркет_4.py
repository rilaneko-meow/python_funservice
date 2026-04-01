from geom_sys import *
from tkinter import *
root=Tk()
root.title('Паркет_4')
canvas=Canvas(root,width=285,height=230,bg='white')
canvas.pack()
def elem(S,q):
    SH=[(-1,-1),(1,-1),(1,1),(-1,1),
        (-1,0),(0,-1),(1,0),(0,1)]
    L=move(S,mlt(SH,q))
    canvas.create_polygon(L[:4],outline='black',
                          fill='lightgray')
    canvas.create_polygon(L[4:],outline='black',
                          fill='white')
# ---------- main --------- #
S=(60,60); q=25
V1=(2*q+5,0)
V2=(0,2*q+5)
for i in range(3):
    for j in range(4):
        w=add(S,mlt(V1,j),mlt(V2,i))
        elem(w,q)

