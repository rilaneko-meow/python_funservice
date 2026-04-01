from tkinter import *
root=Tk()
root.title('Флаг Италии')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()
# -------- параметры ---------
(xs,ys)=(30,20); d=40; w=1.5*d
# ----------------------------
canvas.create_rectangle(xs,ys,xs+w,ys+3*d,fill='#007a33')
xs+=1.5*d
canvas.create_rectangle(xs,ys,xs+w,ys+3*d,fill='#ffffff')
xs+=1.5*d
canvas.create_rectangle(xs,ys,xs+w,ys+3*d,fill='#cb333b')
