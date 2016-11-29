from tkinter import *
from PIL import Image, ImageTk

def resize(img_path, width, height):
    image = Image.open(img_path)
    resized_image = image.resize((50, 50), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()
floor = resize("floor.png",50 ,50)
wall = resize("wall.png", 50, 50)

#initbe mint self.map
wallitems = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
             [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
             [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
             [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]
for i in range(10):
    for j in range(11):
        if wallitems[j][i] == 0:
            canvas.create_image(i*50,j*50, anchor=NW, image=floor)
        else:
            canvas.create_image(i*50,j*50, anchor=NW, image=wall)
root.mainloop()
