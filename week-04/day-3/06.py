# create a 300x300 canvas.
# draw a green 10x10 square to its center.
from tkinter import *
root = Tk()
canv1 = Canvas(root, width = "300", height = "300")
rect1 = canv1.create_rectangle("145","145","155","155")
canv1.pack()
root.mainloop()
