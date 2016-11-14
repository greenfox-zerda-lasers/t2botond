from tkinter import *
import random
import time
import math
root = Tk()

#   ENVIROMENTAL CONSTANTS
canvasheight = 600
canvaswidth = 1200

#      SCREEN CENTER PARAMETERS
t = 3.14
def cent_x(x):
    return x + canvaswidth / 2

def cent_y(x):
    return  x + canvasheight / 2

#   SCREEN
canvas = Canvas(root, width = canvaswidth, height = canvasheight ,bg = '#000000')
canvas.pack()
x = 0
y = 0

# PARAMETRIC STUFF
def funct_x1(t):
    return cent_x(math.sin(t)*100)

def funct_y1(t):
    return cent_y(math.cos(t)*100)

def funct_x2(t):
    return cent_x(math.sin(t)*150)

def funct_y2(t):
    return cent_y(math.cos(t)*150)
#drawing function
def draw ():

        canvas.create_line(funct_x1(t/12), funct_y1(t/12), cent_x(0),cent_y(0), fill = "white")
        canvas.create_line(funct_x2(t), funct_y2(t),  cent_x(0),cent_y(0), fill = "white")

while t < 1000:
    t -= 0.03
    canvas.delete('all')
    time.sleep(0.1)
    draw()
    print(t)
    canvas.update()
root.mainloop()
