# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
from tkinter import *
root = Tk()

def squares(x,y):
    rect1 = canv.create_rectangle(150-(x/2),150-(y/2),150+(x/2),150+(y/2), fill = "green")
    rect1 = canv.create_rectangle(150-(x/3),150-(y/3),150+(x/3),150+(y/3), fill = "grey")
    rect1 = canv.create_rectangle(150-(x/4),150-(y/4),150+(x/4),150+(y/4), fill = "tomato")

canv = Canvas(root, width = 300,height = 300)
squares(150,150)
canv.pack()
root.mainloop()
