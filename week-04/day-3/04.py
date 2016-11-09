# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
from tkinter import *

def drawline(x,y):
    line1 = canv1.create_line(x,y,"150","150")

root = Tk()
canv1 = Canvas(root, width = "300", height = "300")
canv1.pack()

drawline(15,69)
root.mainloop()
