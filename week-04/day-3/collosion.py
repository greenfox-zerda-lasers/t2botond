from tkinter import *
import random
import time
import math
root = Tk()
canvasheight = 600
canvaswidth = 1200

canvas = Canvas(root, width = canvaswidth, height = canvasheight)
canvas.pack()

r = 16
koordx = 16
koordy = canvasheight / 2
xindex = 1
yindex = 1
v = 10
alfa = random.randint(-75,75)
collosion = 0

def _create_circle():
    return canvas.create_oval(koordx-r, koordy-r, koordx+r, koordy+r,fill = 'black')

while collosion <10:
     canvas.delete("all")
     koordx=koordx+(math.sin(((alfa+90)/180)*3.141592654)*v)*xindex   #*u; iranyindex
     koordy=koordy+(math.cos(((alfa+90)/180)*3.141592654)*v)*yindex    #*x; iranyindex

     if koordx//1 >= canvaswidth-r:
         xindex = xindex *(-1)
         collosion+=1
     if koordx//1 <= r:
         xindex = xindex *(-1)
         collosion+=1
     if koordy//1 >= canvasheight-r:
         yindex = yindex *(-1)
         collosion+=1
     if koordy//1 <= r:
         yindex = yindex *(-1)
         collosion+=1

     _create_circle()
     time.sleep(0.02)
     canvas.update()
root.mainloop()
