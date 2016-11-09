# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
from tkinter import *
root = Tk()
canvi = Canvas(root, width = 300, height = 300)

def linedrawer(x,y):
    canvi.create_line(x,y,150,150)
    i = 0
    while i < 300:
        canvi.create_line(i,0,150,150)
        canvi.create_line(0,i,150,150)
        canvi.create_line(300,i,150,150)
        canvi.create_line(i,300,150,150)
        i+=20
linedrawer(30,59)
canvi.pack()
root.mainloop()
