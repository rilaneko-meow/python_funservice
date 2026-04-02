import time
import tkinter as tk
from asyncio import sleep
from tkinter import ttk
import math

import random

# Главное окно
root = tk.Tk()
root.title("Подборщик цвета")
root.geometry("750x450")
root.resizable(False, False)

class Meta:
    selected = []
    game = True


def set_game(v):
    game = v

def donya():
    reset_canvas(canvas)

def generate(canvas: tk.Canvas):
    reset_canvas(canvas)
    for i in range(5):
        for j in range(3):
            if random.randint(0,1):
                Meta.selected.append((i,j))
                canvas.create_oval(i*150,j*150,(i+1)*150,(j+1)*150, fill='#00FF00')
    print(Meta.selected)
    Meta.game = True
    root.after(3000,donya)

def reset_canvas(c:tk.Canvas, lines=True):
    canvas.create_rectangle(0,0,750,450,fill="#aaddcc")
    if lines:
        for i in range(6):
            canvas.create_line(0+i*150,0,0+i*150, 150*3)
        for i in range(4):
            canvas.create_line(0,0+i*150,150*5, 0+i*150)
    pass

def count_rect(x,y):
    x_r = math.floor(x / 150)
    y_r = math.floor(y / 150)

    return (x_r,y_r)

def onClick(event):

    if not Meta.game:
        # todo рестарт
        generate(canvas)
        return

    rr = count_rect(event.x,event.y)
    print(event.x, event.y, rr, Meta.selected)
    if rr in Meta.selected:
        canvas.create_oval(rr[0]*150,rr[1]*150,(rr[0]+1)*150,(rr[1]+1)*150, fill='#00FF00')
        Meta.selected.remove(rr)

        if len(Meta.selected) < 1:
            # Todo выиграл
            reset_canvas(canvas, False)
            canvas.create_text(400, 100,text = 'Победил')
            canvas.create_text(400, 200,text = 'Нажми чтобы сыграть еще раз')
            Meta.game = False
            pass
    else:
        reset_canvas(canvas, False)
        canvas.create_text(400, 100,text = 'Проиграл')
        canvas.create_text(400, 250,text = 'Нажми чтобы сыграть еще раз')
        Meta.game = False
    pass

canvas = tk.Canvas(root,
                width=750,height=450,bg='#aaddcc')
canvas.bind('<Button-1>',onClick)

canvas.pack()

reset_canvas(canvas)
generate(canvas)

root.mainloop()