from tkinter import *
from collosion2 import colltop, collbottom, collleft, collright
import random
import time
import math
root = Tk()

#   ENVIROMENTAL CONSTANTS
a = 0.2
canvasheight = 600
canvaswidth = 1200

#   BEGINNING VALUE
r = 16
x = 50
y = 20

vx = 14
vy = 0
timer = 1
t = 1

#   BALL
def ball(x, y):
    return canvas.create_oval(x-r, y-r, x+r, y+r)

#   SCREEN
canvas = Canvas(root, width = canvaswidth, height = canvasheight)
canvas.pack()

while timer < 80:
    timer += 1

    #vizszintes
    ball(x, 20)

    #fuggoleges
    ball(50, y)

    #ferden
    ball(x, y)

    #vizszintes sebesseg
    x += vx * (timer- (timer-1))
    #fuggoleges sebesseg
    y += ((a / 2) * timer ** 2)-((a / 2) * (timer-1) ** 2)

    time.sleep(0.1)
    canvas.update()

#    if timer%5 == 0 :
#        canvas.create_line(50, y,x,y, fill = "red" )
#        canvas.create_line(x, 16,x,y, fill = "red" )
root.mainloop()
