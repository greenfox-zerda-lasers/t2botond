from tkinter import *
import math
import time
root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

m = 3**(1/2)/2
size = 600
def six(x,y,size):
#    time.sleep(0.01)
    canvas.create_polygon(x,y,
                          x+(1/3*size),y,
                          x+(1/2*size),y+(size*m/3),
                          x+(1/3*size),y+(2/3*size*m),
                          x,y+(2/3*size*m),
                          x-(1/6*size),y+size*m/3, fill = "white",outline= 'tomato')
    canvas.update()


    if size > 10:
        six(x,y,size/3)
        six(x+size*2/9,y,size/3)
        six(x,y+(size*4/9*m),size/3)
        six(x+size*2/9,y+(size*4/9*m),size/3)
        six(x-size/9,y+(size*2/9*m),size/3)
        six(x+size*3/9,y+(size*2/9*m),size/3)
six(150,0,600)
root.mainloop()
