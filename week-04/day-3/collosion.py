from tkinter import *
import random
import time
import math
root = Tk()
canvasheight = 600
canvaswidth = 1200

canvas = Canvas(root, width = canvaswidth, height = canvasheight)
canvas.pack()
g = 0.9
t = 0
r = 16
v1 = 0
out = False
koordx = 50
koordy = canvasheight / 2
xindex = 1
yindex = -1
vx = random.randint(1, 10 )
vy = random.randint(1, 2 )
#alfa = random.randint(0, 360 )
collosion = 0
bounceforce = 0

def _create_circle():
    return canvas.create_oval(koordx-r, koordy-r, koordx+r, koordy+r)

while collosion < 10 :
#     canvas.delete("all")
     koordx += vx * xindex
     koordy += vy * yindex + (v1)
     t += 1
     v1 = (g/2)*t**2/5
     if out == False :
        if koordx >= canvaswidth - r :
             xindex = xindex * (-1)
             collosion += 1
             out = True
        if koordx <= r :
             xindex = xindex *(-1)
             collosion += 1
             out = True
        if koordy >= canvasheight -r :
             yindex = yindex * (-1)
             collosion += 1
             vy += v1
             v1 = 0
             t = 0
             vy = -vy
             out = True
        if koordy <= r :
             yindex = yindex * (-1)
             collosion += 1
             out = True
     elif  koordx < canvaswidth - r or koordx > r or koordy < canvasheight -r or koordy > r :
        out = False

     _create_circle()
     time.sleep(0.1)
     canvas.update()
root.mainloop()
