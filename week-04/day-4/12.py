
from tkinter import *
root = Tk()
canvas = Canvas(root, width = 600, height = 600, bg = 'yellow')
canvas.pack()

def pattern(x,y,k):
    canvas.create_rectangle(x,y,x+k,y+k)
    if k > 2:
        pattern(x , y+k/3 , k/3)
        pattern(x+k*(2/3) , y+k/3 , k/3)
        pattern(x+k/3, y , k/3)
        pattern(x+k/3, y+k*(2/3), k/3)

pattern(0,0,600)
root.mainloop()
