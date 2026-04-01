from tkinter import *
root=Tk()
root.title('Флаг Швейцарии')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()
# -------- параметры ---------
(xs,ys)=(30,20); d=40; 
# ----------------------------
canvas.create_rectangle(xs,ys,xs+3*d,ys+3*d,fill='#da291c')
canvas.create_rectangle(xs+1.2*d,ys+0.5*d,xs+1.8*d,ys+2.4*d,
                        width=0,fill='#ffffff',)
xs+=1.5*d
ys+=0.1*d
canvas.create_rectangle(xs-d,ys+1.7*d,xs+d,ys+1.1*d,
                        width=0,fill='#ffffff')
