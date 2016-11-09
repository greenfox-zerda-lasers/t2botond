# create a 300x300 canvas.
# fill it with a checkerboard pattern.
from tkinter import *
root = Tk()
can = Canvas(root, width=300, height=300)
j=0
while j <= 300:
    i=0
    while i <= 300:
        can.create_rectangle(i,j,i+15,j+15, fill = "black")
        can.create_rectangle(i+15,j,i+30,j+15, fill = "white")
        can.create_rectangle(i,j+15,i+15,j+30, fill = "white")
        can.create_rectangle(i+15,j+15,i+30,j+30, fill = "black")
        i+=30
    j+=30

can.pack()
root.mainloop()
