from geom_sys import *
from tkinter import *
root=Tk()
root.title('Паркет_6')
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
# ---------- main --------- #
S=(145,115)
q=80
for i in range(4):
    elem(S,q) 
    q=q/2 
