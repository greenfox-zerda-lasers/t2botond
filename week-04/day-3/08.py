# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
from tkinter import *
root = Tk()

def drawrects(x,y):
    rect1 = canv1.create_rectangle(x ,y ,x+50,y+50, fill = "red")
    rect2 = canv1.create_rectangle(x+50,y+50,x+100,y+100, fill = "blue")
    rect3 = canv1.create_rectangle(x+100,y+100,x+150,y+150, fill = "green")

canv1 = Canvas(root, width = "300", height = "300")

drawrects(50,20)
canv1.pack()
root.mainloop()
