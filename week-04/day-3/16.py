# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
from tkinter import *
import random
import time
root = Tk()
p = 600

def generate_color():
    w=random.randrange(0, 9)
    color = '#'+str(w)*3
    return color

canvas = Canvas(root, width = p, height = p,bg ='black')
canvas.pack()
for i in range(150):
    x = random.randrange(5,p+3,1)
    y = random.randrange(5,p+3,1)
    canvas.create_rectangle(x-1,y-1,x+1,y+1, fill = generate_color())
    time.sleep(0.1)
    canvas.update()
root.mainloop()
