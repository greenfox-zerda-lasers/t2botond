# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
from tkinter import *
root = Tk()

import random

def generate_color():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color

def recbow(m):
    import random
    k = 0
    i=0
    while (k+10)*2 < (300-m):
        rect=canvas.create_rectangle(10+k,10+k,290-k,290-k, fill = generate_color())
        i+=1
        k+=10
canvas = Canvas(root, width = 300, height = 300)
recbow(150)
canvas.pack()
root.mainloop()
