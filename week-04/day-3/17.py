from tkinter import *
import random
import time
import math
root = Tk()
p = 600

canvas = Canvas(root, width = p, height = p)
canvas.pack()
collusion = 0
y1 = p/2
r1 = 16
sebes = 5
szog = 30
u = 1
t = 50
z = p/2
def _create_circle( x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

while collusion < 5:
     _create_circle(x1,y1,16)
     x=t+(math.sin(((szog+90)/180)*3.141592654)*sebes)*u;
     y=z+(math.cos(((szog+90)/180)*3.141592654)*sebes)*x;
     if(t<16) :
        u=u*(-1)
        n+=1
        collosion=n
        p-16
     if(t>(p-16)):
        u=u*(-1)
        n+=1
        collosion=n
     if(z<16):
        x=x*(-1)
        n+=1
        i=n
        p-16;
        collosion=n
     if(z>p):
        x=x*(-1)
        n+=1
        collosion=n
root.mainloop()
