from tkinter import *
root=Tk()
root.title('Проба')
canvas=Canvas(root,width=450,height=300)
canvas.pack()
x, y = 200, 210

spline = canvas.create_line(x,y,x+2*70,y,x+2*70,y-2*70,
                            x-2*70,y-2*70,x-2*70,y,x,y,
                                width=2,fill='black',smooth=True)

#200,80,70
'''poly = canvas.create_polygon(50,90,50+150,90,50+150,90+90,50,90+90,
                             width=2,outline='black',
                             fill='red',stipple='gray50',smooth=True)'''

'''poly = canvas.create_polygon(x,y,x+size,y,x+size,y+size,x,y+size,
                                 width=2,outline=s,fill='gray',
                                 stipple='gray12',smooth=True)'''

'''x1, y1, x2, y2 = 20, 30, 200, 120
arc1 = canvas.create_arc(x1,y1,x1+25,y1+20,
                        start=90,extent=90,
                        width=2,outline='black',
                        style='arc')
arc2 = canvas.create_arc(x2-30,y1,x2,y1+30,
                        start=0,extent=90,
                        width=2,outline='black',
                        style='arc')
arc3 = canvas.create_arc(x2-40,y2-30,x2,y2,
                        start=270,extent=90,
                        width=2,outline='black',
                        style='arc')
arc4 = canvas.create_arc(x1,y2-20,x1+25,y2,
                        start=180,extent=90,
                        width=2,outline='black',
                        style='arc')

line1=canvas.create_line(x1+12,y1,x2-12,y1,width=2,fill='black')
line2=canvas.create_line(x2,y1+9,x2,y2-9,width=2,fill='black')
line3=canvas.create_line(x2-12,y2,x1+12,y2,width=2,fill='black')
line4=canvas.create_line(x1,y2-7,x1,y1+7,width=2,fill='black')'''


'''line1=canvas.create_line(20,30,200,30,width=2,fill='black')
line2=canvas.create_line(200,30,200,120,width=2,fill='black')
line3=canvas.create_line(20,120,200,120,width=2,fill='black')
line4=canvas.create_line(20,120,20,30,width=2,fill='black')'''
