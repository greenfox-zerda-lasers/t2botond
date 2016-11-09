# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.
from tkinter import *
def drawline(x,y):
    root = Tk()
    canv1 = Canvas(root, width = "300", height = "300")
    line1 = canv1.create_line(x,y,x+50,y)
    canv1.pack()
    root.mainloop()
drawline(15,19)
