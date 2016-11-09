# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
from tkinter import *

root = Tk()
canv1 = Canvas(root, width = "300", height = "300")
line1 = canv1.create_line("10","10","290","10")
line2 = canv1.create_line("290","10","290","290", fill = "#16F6F6")
line3 = canv1.create_line("10","290","290","290",fill = "#d89652")
line4 = canv1.create_line("10","290","10","10",fill = "#F23654")
canv1.pack()
root.mainloop()
