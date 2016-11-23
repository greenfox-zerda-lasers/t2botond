from tkinter import *
from PIL import Image, ImageTk

def resize(img_path, width, height):
    image = Image.open(img_path)
    resized_image = image.resize((50, 50), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

canvas_width = 720
canvas_height = 720

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()
floor = resize("floor.png",50 ,50)
wall = resize("wall.png", 50, 50)

root.mainloop()



    def tile_pattern(self, game_field_elements):
        for i in range(10):
            for j in range(10):
                if game_field_elements[j][i] == 0:
                    canvas.create_image(i*50,j*50, anchor=NW, image=floor)
                else:
                    canvas.create_image(i*50,j*50, anchor=NW, image=wall)
