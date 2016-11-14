from tkinter import *
import math
import time
root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

m = 3**(1/2)/2
size = 600
def triangle(x,y,size):
    time.sleep(0.01)
    canvas.create_polygon(x,y,x+size,y,x+size/2,y+size*m, fill = "white",outline= 'tomato')
    canvas.update()


    if size > 10:
        triangle(x,y,size/2)
        triangle(x+size/2,y,size/2)
        triangle(x+size/4,y+(m*size)/2,size/2)

triangle(0,0,600)
root.mainloop()
