from tkinter import *
from PIL import Image, ImageTk

def resize(img_path, width, height):
    image = Image.open(img_path)
    resized_image = image.resize((50, 50), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

canvas_width = 720
canvas_height = 720

class Map:
    print("Megy a class 1")
    def __init__(self):
        print("Megy a class 2")
        game_field_elements =  [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
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

        floor = resize("floor.png",50 ,50)
        wall = resize("wall.png", 50, 50)
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        print("Megy a class 2")
        root = Tk()
        canvas = Canvas(root, width = 720, height = 720)
        canvas.pack()
        for i in range(10):
            for j in range(10):
                if self.game_field_elements[j][i] == 0:
                    canvas.create_image(i*50,j*50, anchor=NW, image=floor)
                else:
                    canvas.create_image(i*50,j*50, anchor=NW, image=wall)
        floor = resize("floor.png",50 ,50)
        wall = resize("wall.png", 50, 50)

        root.mainloop()
