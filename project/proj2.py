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
    opened_1 = (-1, -1)
    opened_2 = (-1, -1)
    game = True
    state = 0


def set_game(v):
    game = v


def donya():
    reset_canvas(canvas)


def generate(canvas: tk.Canvas):
    reset_canvas(canvas)
    rr = []
    for i in range(10):
        rr.append(i)
        rr.append(i)

    for i in range(5):
        for j in range(4):
            Meta.selected[i][j] = rr[len(rr)]
    print(Meta.selected)
    Meta.game = True


def reset_canvas(c: tk.Canvas, lines=True):
    canvas.create_rectangle(0, 0, 750, 600, fill="#aaddcc")
    for i in range(5):
        for j in range(4):
            if Meta.selected[i][j] > 0:
                # todo draw rect
                pass
    if Meta.state == 1:
        # todo draw opened rect
        pass
    if Meta.state == 2:
        #todo draw bot then decay
        root.after(1000, donya)
        pass
    pass


def count_rect(x, y):
    x_r = math.floor(x / 150)
    y_r = math.floor(y / 150)

    return (x_r, y_r)


def onClick(event):
    if not Meta.game:
        # todo рестарт
        generate(canvas)
        return

    rr = count_rect(event.x, event.y)


canvas = tk.Canvas(root,
                   width=750, height=600, bg='#aaddcc')
canvas.bind('<Button-1>', onClick)

canvas.pack()

reset_canvas(canvas)
generate(canvas)

root.mainloop()
