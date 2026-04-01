from geom_sys import *
from time import *
from tkinter import *
root=Tk()
root.title('Часы')
canvas=Canvas(root,width=260,height=260,bg='white')
canvas.pack()

# параметры-----------
R1= 40 # длина часовой стрелки
R2= 60 # длина минутной стрелки
R3= 70 # радиус внутреннего круга и секундной стрелки
R4= 90 # срединный радиус числовых отметок
R5=110 # внешний радиус часов
# ---------------------

(xs,ys)=S=(130,130)
create_circle(canvas,S,R5,width=3,
              outline='black',fill='#ffeeff')
create_circle(canvas,S,R3,outline='',fill='white')
create_circle(canvas,S,7,outline='',fill='blue')

# отметки на циферблате
hour=0
for i in range(1,61):
    fi=90-6*i
    if i%5==0:
        hour+=1
        P=ps2ds(S,(R1,fi))
        Q=ps2ds(S,(R3,fi))
        T=ps2ds(S,(R4,fi))
        canvas.create_text(T,text=str(hour),
                           font=('Courier New',20,'bold'))
else:
    P=ps2ds(S,(R2,fi))
    Q=ps2ds(S,(R3,fi))
    canvas.create_line(P,Q)

# движение стрелок
for k in range(30):
    tm=localtime()
    sfi=6*tm.tm_sec
    mfi=6*(tm.tm_min+sfi/360)
    h=tm.tm_hour%12
    hfi=30*(h+mfi/360)
    Ph=ps2ds(S,(R1,90-hfi))
    Pm=ps2ds(S,(R2,90-mfi))
    Ps=ps2ds(S,(R3,90-sfi))
    idh=canvas.create_line(S,Ph,width=7,fill='blue')
    idm=canvas.create_line(S,Pm,width=3,fill='blue')
    ids=canvas.create_line(S,Ps,width=1,fill='red')
    canvas.update()
    sleep(1)
    canvas.delete(ids,idm,idh)
idh=canvas.create_line(S,Ph,width=7,fill='blue')
idm=canvas.create_line(S,Pm,width=3,fill='blue')
ids=canvas.create_line(S,Ps,width=1,fill='red')
