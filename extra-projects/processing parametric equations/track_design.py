from tkinter import *
from random import randint, choice
import time
import math
root = Tk()

#   ENVIROMENTAL CONSTANTS
canvasheight = 600
canvaswidth = 1200

#      SCREEN CENTER PARAMETERS
t = 0
def cent_x(x):
    return x + canvaswidth / 2

def cent_y(x):
    return  x + canvasheight / 2

#   SCREEN
canvas = Canvas(root, width = canvaswidth, height = canvasheight ,bg = '#000000')
canvas.pack()
x = 0
y = 0
color = []
# PARAMETRIC STUFF
def funct_x1(t):
    return cent_x(math.sin(t)+((math.sin(t/10)*100) + 155))

def funct_y1(t):
    return cent_y(math.cos(t)+(math.sin(t/23)*120) -170)

def funct_x2(t):
    return cent_x(math.sin(t)+(math.sin(t)+((math.sin(-t/10)*133) + math.sin(t / 15/9) * 29 - 200)))

def funct_y2(t):
    return cent_y(math.cos(t)+(math.cos(t/-20)*200) + 96)
#drawing function
def draw ():
    if len(color) > 0 :
        color.pop(0)
    def gen_hex_colour_code(color):
        color.append('#'+''.join([choice('0123456789ABCDEF') for i in range(6)]))
        return color
    for i in range(25):
        gen_hex_colour_code(color)
    #    canvas.create_line(funct_x1(t+i), funct_y1(t+i), funct_x2(t+i), funct_y2(t+i), fill = color[i])

    canvas.create_line(funct_x1(t+i+1), funct_y1(t+i+1), funct_x1(t+i), funct_y1(t+i), fill = "white")
    canvas.create_line(funct_x2(t+i+1), funct_y2(t+i+1), funct_x2(t+i), funct_y2(t+i), fill = "white")


while t < 1000:
    t += 0.8
    #canvas.delete('all')
    time.sleep(0.02)
    draw()
    canvas.update()
root.mainloop()
