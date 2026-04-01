from time import *
from tkinter import *
root=Tk()
root.title('Цифровые часы')
canvas=Canvas(root, width=260, height=80, bg='#aaccff')
canvas.pack()

for k in range(20):
    res=ctime().split()[3]
    tm=canvas.create_text(130,40,text=res,
                          font=('Courier New',32,'bold'))
    canvas.update()
    sleep(1)
    canvas.delete(tm)
canvas.create_text(130,40,text=res,
                   font=('Courier New',32,'bold'))

