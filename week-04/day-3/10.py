# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.
from tkinter import *
root = Tk()

def rect20(s):
    z=0
    for i in range(20):
        rect1 = canv.create_rectangle(150-(s/2)-z,150-(s/2)-z,150+(s/2)+z,150+(s/2)+z)
        z+=3
canv = Canvas(root, width = 300, height = 300)
rect20(20)
canv.pack()
root.mainloop()
