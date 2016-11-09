# create a 300x300 canvas.
# draw its diagonals in green.
from tkinter import *

root = Tk()
canv1 = Canvas(root, width = "300", height = "300")
line1 = canv1.create_line("0","0","300","300", fill = "green")
line2 = canv1.create_line("0","300","300","000", fill = "green")
canv1.pack()
root.mainloop()
