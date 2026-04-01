from tkinter import *
root=Tk()
root.title('Узор_1')
canvas=Canvas(root,width=550,height=250,bg='white')
canvas.pack()
# --------- параметры ---------
(xs,ys)=(20,150); R=10; dR=-5
# -----------------------------
for r in range(R,0,dR):
        canvas.create_oval(xs-r, ys-r, xs+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+5,0,dR-3):
        canvas.create_oval((xs+21)-r, ys-r, (xs+21)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+10,0,dR-6):
        canvas.create_oval((xs+49)-r, ys-r, (xs+49)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+15,0,dR-9):
        canvas.create_oval((xs+84)-r, ys-r, (xs+84)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+20,0,dR-12):
        canvas.create_oval((xs+126)-r, ys-r, (xs+126)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+25,0,dR-15):
        canvas.create_oval((xs+175)-r, ys-r, (xs+175)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+30,0,dR-18):
        canvas.create_oval((xs+230)-r, ys-r, (xs+230)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+35,0,dR-21):
        canvas.create_oval((xs+292)-r, ys-r, (xs+292)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+40,0,dR-23):
        canvas.create_oval((xs+360)-r, ys-r, (xs+360)+r, ys+r,
                           width=2, outline='black', fill='white')
for r in range(R+45,0,dR-23):
        canvas.create_oval((xs+435)-r, ys-r, (xs+435)+r, ys+r,
                           width=2, outline='black', fill='white')
