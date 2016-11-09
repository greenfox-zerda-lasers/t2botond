# create a 300x300 canvas.
# fill it with four different size and color rectangles.
from tkinter import *
root = Tk()
canv1 = Canvas(root, width = "300", height = "300")
rect1 = canv1.create_rectangle("11","11","150","150", fill = "red")
rect2 = canv1.create_rectangle("11","150","150","300", fill = "blue")
rect3 = canv1.create_rectangle("150","11","300","150", fill = "green")
canv1.pack()
root.mainloop()
