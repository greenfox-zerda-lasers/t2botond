# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.
from tkinter import *

root = Tk()
canv1 = Canvas(root, width = "300", height = "300", bg="black")
canv1.pack()
root.mainloop()
