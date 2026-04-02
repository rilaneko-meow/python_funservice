import time
import tkinter as tk
from asyncio import sleep
from tkinter import ttk
import math

import random

# Главное окно
root = tk.Tk()
root.title("Подборщик цвета")
root.geometry("600x600")
root.resizable(False, False)


class Meta:
    selected = [[random.randint(0, 1) for j in range(4)] for i in range(4)]


def count_rect(x, y):
    x_r = math.floor(x / 150)
    y_r = math.floor(y / 150)

    return (x_r, y_r)


def generate():
    Meta.selected = [[random.randint(0, 1) for j in range(4)] for i in range(4)]
    redraw(canvas)


def redraw(canvas, lines=True):
    canvas.create_rectangle(0, 0, 600, 600, fill="#aaddcc")
    if lines:
        for i in range(4):
            canvas.create_line(0 + i * 150, 0, 0 + i * 150, 150 * 4)
        for i in range(4):
            canvas.create_line(0, 0 + i * 150, 150 * 4, 0 + i * 150)
        for i in range(4):
            for j in range(4):
                c = '#FF0000'
                if Meta.selected[i][j]:
                    c = "#0000FF"
                canvas.create_oval(i * 150, j * 150, (i + 1) * 150, (j + 1) * 150, fill=c)


def check():
    r = 0
    for i in range(4):
        for j in range(4):
            r += Meta.selected[i][j]
    return r == 0 or r == 16


def flip(a):
    if a:
        return 0
    else:
        return 1


def onClick(event):
    rr = count_rect(event.x, event.y)
    print(event.x, event.y, rr, Meta.selected)
    prev = Meta.selected[rr[0]][rr[1]]
    for i in range(4):
        Meta.selected[rr[0]][i] = flip(Meta.selected[rr[0]][i])
        Meta.selected[i][rr[1]] = flip(Meta.selected[i][rr[1]])
    Meta.selected[rr[0]][rr[1]] = flip(prev)
    if not check():
        redraw(canvas)
    else:
        canvas.create_rectangle(0, 0, 600, 600, fill="#00FF00")
        canvas.create_text(300,300,text = "Победил")
        root.after(2000,generate)


canvas = tk.Canvas(root,
                   width=600, height=600, bg='#aaddcc')
canvas.bind('<Button-1>', onClick)

canvas.pack()

redraw(canvas)
generate()

root.mainloop()
