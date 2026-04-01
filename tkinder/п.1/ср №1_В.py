from tkinter import *
root=Tk()
root.title('Прямоугольник')
canvas=Canvas(root,width=250,height=250)
canvas.pack()

def roundrect(x,y,size,s,**kw):
    poly = canvas.create_polygon(x,y,x+size,y,x+size,y+(2/3)*size,x,y+(2/3)*size,
                                 width=2,outline=s,fill='gray',
                                 stipple='gray12',smooth=True)

    text=canvas.create_text(x+60,y+35,
                            text='',fill='blue',
                            font=('Comic Sans MS',30//2,'bold'))

    if kw.get('text')!=None:
        canvas.itemconfig(text,text=kw['text'])

roundrect(20,50,120,'black',text='Hello')
#roundrect(50,90,200,'black')

