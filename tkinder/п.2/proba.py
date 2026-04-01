from tkinter import *
root=Tk()
root.title('Узор_3')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

'''def inter(A,B,q):
    (xa,ya)=A
    (xb,yb)=B
    return (xa+q*(xb-xa), ya+q*(yb-ya))

L=[(100,60),(60, 90),(60,120),(100,150),(140,120),(140,90)]
q=0.2; n=10
for i in range(n):
    canvas.create_line(L,L[0],fill='red')
    L=[inter(L[i],L[(i+1)%6],q) for i in range(6)]'''

x1, x2, x3 = 100, 60, 140
y1, y2, y3, y4 = 60, 90, 120, 150
line1=canvas.create_line(x1,y1,x2,y2,width=2,fill='black')
#line2=canvas.create_line(x2,y2,x2,y3,width=2,fill='black')
#line3=canvas.create_line(x2,y3,x1,y4,width=2,fill='black')
#line4=canvas.create_line(x1,y4,x3,y3,width=2,fill='black')
#line5=canvas.create_line(x3,y3,x3,y2,width=2,fill='black')
#line6=canvas.create_line(x3,y2,x1,y1,width=2,fill='black')
