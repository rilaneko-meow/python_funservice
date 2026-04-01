from tkinter import *
root=Tk()
root.title('Прямоугольник')
canvas=Canvas(root,width=450,height=300)
canvas.pack()

def roundrect(x,y,size,s,**kw):
    spline = canvas.create_line(x,y,x+2*size,y,x+2*size,y-2*size,x-2*size,y-2*size,x-2*size,y,x,y,
                                width=2,fill=s,smooth=True)

    text=canvas.create_text(x,y//1.5,
                            text='',fill='blue',
                            font=('Comic Sans MS',30//2,'bold'))

    if kw.get('text')!=None:
        canvas.itemconfig(text,text=kw['text'])
    

roundrect(200,210,70,'black',text='Hello')
