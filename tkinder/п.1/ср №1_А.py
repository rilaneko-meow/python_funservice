from tkinter import *
root=Tk()
root.title('Прямоугольник')
canvas=Canvas(root,width=200,height=240)
canvas.pack()
def roundrect(x1,y1,x2,y2,s,**kw):
    arc1 = canvas.create_arc(x1,y1,x1+25,y1+20,
                        start=90,extent=90,
                        width=2,outline=s,
                        style='arc')
    arc2 = canvas.create_arc(x2-30,y1,x2,y1+30,
                            start=0,extent=90,
                            width=2,outline=s,
                            style='arc')
    arc3 = canvas.create_arc(x2-40,y2-30,x2,y2,
                            start=270,extent=90,
                            width=2,outline=s,
                            style='arc')
    arc4 = canvas.create_arc(x1,y2-20,x1+25,y2,
                            start=180,extent=90,
                            width=2,outline=s,
                            style='arc')
    line1=canvas.create_line(x1+12,y1,x2-12,y1,width=2,fill=s)
    line2=canvas.create_line(x2,y1+9,x2,y2-9,width=2,fill=s)
    line3=canvas.create_line(x2-12,y2,x1+12,y2,width=2,fill=s)
    line4=canvas.create_line(x1,y2-7,x1,y1+7,width=2,fill=s)

    text=canvas.create_text((x2-x1)//1.7,(y2-y1)//1.3,
                            text='',fill='blue',
                            font=('Comic Sans MS',30//2,'bold'))

    if kw.get('text')!=None:
        canvas.itemconfig(text,text=kw['text'])

roundrect(20,30,200,120,'black',text='Hello')
#roundrect(50,80,150,200,'black')
