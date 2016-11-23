from tkinter import *
from PIL import Image, ImageTk
import Character

class Draw:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 620, height = 620)
        self.canvas.pack()
        self.floor = self.resize("floor.png",50 ,50)
        self.wall = self.resize("wall.png", 50, 50)
        self.herofront = self.resize("hero-down.png", 50, 50)
        self.heroback = self.resize("hero-up.png", 50, 50)
        self.heroleft = self.resize("hero-left.png", 50, 50)
        self.heroright = self.resize("hero-right.png", 50, 50)
        self.boss = self.resize("boss.png", 50, 50)
        self.skeleton = self.resize("skeleton.png", 50, 50)
        self.hero_id = None
        self.boss_id = None
        self.skeleton_id = None

    def resize(self, img_path, width, height):
        image = Image.open(img_path)
        resized_image = image.resize((50, 50), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def draw_background(self, mapdata):
        for i in range(10):
            for j in range(11):
                if mapdata[j][i] == 0:
                    self.canvas.create_image(i*50,j*50, anchor=NW, image=self.floor)
                else:
                    self.canvas.create_image(i*50,j*50, anchor=NW, image=self.wall)

    def draw_hero_front(self, x, y):
        self.canvas.delete(self.hero_id)
        self.hero_id = self.canvas.create_image(x*50,y*50, anchor=NW, image=self.herofront)

    def draw_hero_back(self, x, y):
        self.canvas.delete(self.hero_id)
        self.hero_id =self.canvas.create_image(x*50,y*50, anchor=NW, image=self.heroback)

    def draw_hero_left(self, x, y):
        self.canvas.delete(self.hero_id)
        self.hero_id =self.canvas.create_image(x*50,y*50, anchor=NW, image=self.heroleft)

    def draw_hero_right(self, x, y):
        self.canvas.delete(self.hero_id)
        self.hero_id =self.canvas.create_image(x*50,y*50, anchor=NW, image=self.heroright)

    def draw_boss(self, x, y):
        self.canvas.delete(self.boss_id)
        self.boss_id = self.canvas.create_image(x*50,y*50, anchor=NW, image=self.boss)

    def draw_skeletongroup(self, sklist):
        for i in range(len(sklist)):
    #        self.canvas.delete(self.skeleton_id)
            x = sklist[i][0]
            y = sklist[i][1]
            self.skeleton_id = self.canvas.create_image(x*50,y*50, anchor=NW, image=self.skeleton)

    def launch_screen(self):
        self.root.mainloop()

    def thing(event):
            print(event)
