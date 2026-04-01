from time import *
from geom_sys import *
from tkinter import *
root=Tk()
root.title('Бильярд')
canvas=Canvas(root,width=220,height=200,bg='white')
canvas.pack()

# задаём параметры стола и шара
(x1,y1)=(20,20)
(x2,y2)=(200,180)
(x,y)=(30,30); R=10
(Vx,Vy)=(10,10)
# ------------------------------

canvas.create_rectangle(x1,y1,x2,y2,outline='red')
for k in range(121):
    if k==0:
        A=(x,y)
        ball=create_circle(canvas,A,R,fill='green')
    else:
        if x+Vx-R<x1 or x+Vx+R>x2: Vx=-Vx
        if y+Vy-R<y1 or y+Vy+R>y2: Vy=-Vy
        B=(x+Vx,y+Vy)
        canvas.create_line(A,B,)
        canvas.move(ball,Vx,Vy)
        (xL,yU,xR,yD)=canvas.coords(ball)
        x=(xL+xR)//2; y=(yU+yD)//2
        canvas.update()
        sleep(0.05)
        A=B

