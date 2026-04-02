import random
import tkinter as tk
import math

# Главное окно
root = tk.Tk()
root.title("Подборщик цвета")
root.geometry("600x600")
root.resizable(False, False)
# ------------------------------------------------------
class Meta:
    cnt = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,0]]
    abs = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,0]]
    pass

def generate():
    rr = (3,3)
    rcells = []
    rcell = (-1,-1)
    for i in range(random.randint(10,100)):
        if rr[0] > 0 and Meta.cnt[rr[0] - 1][rr[1]]:
            rcells.append( (rr[0] - 1, rr[1]))
        if rr[0] < 3 and Meta.cnt[rr[0] + 1][rr[1]]:
            rcells.append((rr[0] + 1, rr[1]))
        if rr[1] > 0 and Meta.cnt[rr[0]][rr[1] - 1]:
            rcells.append((rr[0], rr[1] - 1))
        if rr[1] < 3 and Meta.cnt[rr[0]][rr[1] + 1]:
            rcells.append((rr[0], rr[1] + 1))

        rcell = rcells[random.randint(0,len(rcells)-1)]

        if rcell[0] == -1 or rcell[1] == -1:
            continue
        Meta.cnt[rr[0]][rr[1]] = Meta.cnt[rcell[0]][rcell[1]]
        rr = rcell
        Meta.cnt[rcell[0]][rcell[1]] = 0
    draw()
    pass

def draw():
    canvas.create_rectangle(0,0,600,600, fill="#aaddcc")
    for i in range(4):
        for j in range(4):
            if Meta.cnt[i][j] != 0:
                canvas.create_rectangle(i*150,j*150,(i+1)*150,(j+1)*150,fill="#aa55cc")
                canvas.create_text(i*150+75, j*150+75, text=Meta.cnt[i][j])


def count_rect(x, y):
    x_r = math.floor(x / 150)
    y_r = math.floor(y / 150)
    return (x_r, y_r)

def on_click(event):
    rr = count_rect(event.x, event.y)
    print(rr)
    rcell = (-1,-1)
    if Meta.cnt[rr[0]][rr[1]] == 0:
        return

    if rr[0]>0 and Meta.cnt[rr[0]-1][rr[1]]==0:
        rcell = (rr[0]-1, rr[1])
    elif rr[0]<3 and Meta.cnt[rr[0]+1][rr[1]]==0:
        rcell = (rr[0]+1, rr[1])
    elif rr[1]>0 and Meta.cnt[rr[0]][rr[1]-1]==0:
        rcell = (rr[0], rr[1]-1)
    elif rr[1]<3 and Meta.cnt[rr[0]][rr[1]+1]==0:
        rcell = (rr[0], rr[1]+1)
    if rcell[0]==-1 or rcell[1]==-1:
        return
    Meta.cnt[rcell[0]][rcell[1]] = Meta.cnt[rr[0]][rr[1]]
    Meta.cnt[rr[0]][rr[1]] = 0
    draw()
    if Meta.cnt == Meta.abs:
        canvas.create_rectangle(0, 0, 600, 600, fill="#00FF00")
        canvas.create_text(300, 300, text="Победил")

        root.after(2000, generate)

    return
# bb -------------------------------
canvas = tk.Canvas(root,
                   width=600, height=600, bg='#aaddcc')
canvas.bind('<Button-1>', on_click)
canvas.pack()

generate()
root.mainloop()