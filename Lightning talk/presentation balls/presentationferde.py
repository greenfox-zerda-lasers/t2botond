from tkinter import *
from collosion2 import colltop, collbottom, collleft, collright
import random
import time
import math
root = Tk()

#   ENVIROMENTAL CONSTANTS
g = 10 / 50
canvasheight = 600
canvaswidth = 1200

#   BEGINNING VALUE
r = 16
x = 50
y = 560

vx = 10
vy = -10
timer = 1
t = 1

#   BALL
def ball(x, y):
    return canvas.create_oval(x-r, y-r, x+r, y+r)

#   SCREEN
canvas = Canvas(root, width = canvaswidth, height = canvasheight)
canvas.pack()

while timer < 100:
    timer += 1

    #ferden
    ball(x, y)

    #vizsyzintes sebesseg
    x += vx * (timer- (timer-1))
    #fuggoleges sebesseg
    y += vy + ((g / 2) * timer ** 2)-((g / 2) * (timer-1) ** 2)


    time.sleep(0.1)
    canvas.update()

root.mainloop()
