import time
import tkinter as tk
from asyncio import sleep
from enum import Flag
from tkinter import ttk
import math

import random

# Главное окно
root = tk.Tk()
root.title("Подборщик цвета")
root.geometry("750x600")
root.resizable(False, False)


class Meta:
    selected = [[-1 for j in range(4)] for i in range(5)]
    opened_1 = (-1, -1)
    opened_2 = (-1, -1)
    game = True
    state = 0


def set_game(v):
    game = v


def donya():
    reset_canvas(canvas)
    Meta.opened_1 = (-1, -1)
    Meta.opened_2 = (-1, -1)
    Meta.state = 0


def generate(canvas: tk.Canvas):
    reset_canvas(canvas)
    rr = []
    for i in range(10):
        rr.append(i)
        rr.append(i)

    for i in range(5):
        for j in range(4):
            k = random.randint(0, len(rr) - 1)
            Meta.selected[i][j] = rr.pop(k)
    reset_canvas(canvas)
    print(Meta.selected)
    Meta.game = True


def reset_canvas(c: tk.Canvas, lines=True):
    canvas.create_rectangle(0, 0, 750, 600, fill="#aaddcc")
    count = 0
    for i in range(5):
        for j in range(4):
            if Meta.selected[i][j] >= 0:
                count+=1
                canvas.create_rectangle(150 * i, 150 * j, 150 * (i + 1), 150 * (j + 1), fill="#009900",
                                        outline="#000000")
                pass
    if count == 0:
        canvas.create_text(300,200,text="Победил")
        root.after(5000,generate, canvas)
        return
    if Meta.state == 1:
        i = Meta.opened_1[0]
        j = Meta.opened_1[1]
        canvas.create_rectangle(150 * i, 150 * j, 150 * (i + 1), 150 * (j + 1), fill="#bbaabb",
                                outline="#000000")
        canvas.create_text(150 * i + 75, 150 * j + 75, text=Meta.selected[i][j])
        # todo draw opened rect

    if Meta.state == 2:
        # todo draw bot then decay
        flag = False
        bg = "#bbaabb"
        if Meta.selected[Meta.opened_1[0]][Meta.opened_1[1]] == Meta.selected[Meta.opened_2[0]][Meta.opened_2[1]]:
            print("pair")
            bg = "#00FF00"
            flag = True

        i = Meta.opened_1[0]
        j = Meta.opened_1[1]
        canvas.create_rectangle(150 * i, 150 * j, 150 * (i + 1), 150 * (j + 1), fill=bg,
                                outline="#000000")
        t1 = Meta.selected[i][j]
        canvas.create_text(150*i+75, 150*j+75, text=Meta.selected[i][j])
        i = Meta.opened_2[0]
        j = Meta.opened_2[1]
        canvas.create_rectangle(150 * i, 150 * j, 150 * (i + 1), 150 * (j + 1), fill=bg,
                                outline="#000000")
        canvas.create_text(150 * i + 75, 150 * j + 75, text=Meta.selected[i][j])
        if flag:
            Meta.selected[Meta.opened_1[0]][Meta.opened_1[1]] = -1
            Meta.selected[Meta.opened_2[0]][Meta.opened_2[1]] = -1

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
    if Meta.state == 0:
        if Meta.selected[rr[0]][rr[1]] == -1:
            return
        Meta.opened_1 = (rr[0], rr[1])
        Meta.state += 1
    elif Meta.state == 1:
        if Meta.selected[rr[0]][rr[1]] == -1 or Meta.opened_1 == rr:
            return
        Meta.opened_2 = (rr[0], rr[1])
        Meta.state += 1
    elif Meta.state == 2:
        return

    reset_canvas(canvas)
    print(rr)


canvas = tk.Canvas(root,
                   width=750, height=600, bg='#aaddcc')
canvas.bind('<Button-1>', onClick)

canvas.pack()

reset_canvas(canvas)
generate(canvas)

root.mainloop()
