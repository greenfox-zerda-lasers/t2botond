from tkinter import *
from collosion import colltop, collbottom, collleft, collright
import random
import time
import math
root = Tk()

#   ENVIROMENTAL CONSTANTS
g = 10
t = 0
canvasheight = 600
canvaswidth = 1200

#   BEGINNING VALUES
r = 16
x = 50
y = canvasheight / 2
collosion = 0
vx = 5
vy = -0
coeff1 = math.sqrt( vx**2 + vy**2)
out = False

#   BALL
def ball(x,y):
    return canvas.create_oval(x-r, y-r, x+r, y+r)

#   SCREEN
canvas = Canvas(root, width = canvaswidth, height = canvasheight)
canvas.pack()

while collosion < 4:
    ball(x, y)
    x += vx
    y += vy + (g / 2) * t ** 2
    t += (0.01 * ( math.sqrt( vx ** 2 + vy ** 2) / coeff1 ))
    print(math.sqrt(vx ** 2 + (vy+(g/2)*t**2) ** 2))
#    time.sleep(0.05)
    canvas.update()

    if out == False :  # If inside clculations resulting two or more out values
        if x <= r :
            vx = collleft(vx)
            collosion += 1
            out = True
        if x >= canvaswidth-r :
            vx = collright(vx)
            collosion += 1
            out = True
        if y <= r :
            vy = colltop(vy, t, g)
            collosion += 1
            t = 0
            out = True
        if y >= canvasheight-r :
            vy = collbottom(vy, t, g)
            t = 0
            print(vy)
            print(t)
            collosion += 1
            out = True
    else:
        if x > r or x < canvaswidth-r or y > r or y < canvasheight-r :
            out = False
            print ("else lefut")

root.mainloop()
