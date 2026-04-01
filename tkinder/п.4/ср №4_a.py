from geom_sys import *
from tkinter import *
root=Tk()
root.title('Узор_2')
canvas=Canvas(root,width=240,height=240,bg='white')
canvas.pack()

n=7
R=50; R1=45; R2=40; R3=35; R4=30
#R=50; R1=45; R2=40; R3=35  
df=360/n
S=(120,120) 
fi=10
for k in range(n*10): 
    (xc,yc)=ps2ds(S,(R,fi)) 
    canvas.create_arc(xc-R,yc-R,xc+R,yc+R,style='arc', 
                    start=fi-df*3,extent=150+df)

    canvas.create_arc(xc-R1,yc-R1,xc+R1,yc+R1,style='arc', 
                    start=fi-df*3,extent=150+df)

    canvas.create_arc(xc-R2,yc-R2,xc+R2,yc+R2,style='arc', 
                    start=fi-df*3,extent=150+df)

    canvas.create_arc(xc-R3,yc-R3,xc+R3,yc+R3,style='arc', 
                    start=fi-df*3,extent=150+df)

    canvas.create_arc(xc-R4,yc-R4,xc+R4,yc+R4,style='arc', 
                    start=fi-df*3,extent=150+df)

    
    fi=fi+df
