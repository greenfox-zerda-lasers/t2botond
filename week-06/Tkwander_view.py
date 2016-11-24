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
        self.display_id = None
        self.enemydisplay_id = None
        self.diplay_killed = None
        self.skeleton_idlist = [[]]

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

    def draw_display(self, sp, dp, hp, key):
        keyvalue = "None"
        if key == True:
            keyvalue = "Collected!"
        self.canvas.delete(self.display_id)
        self.display_id = self.canvas.create_text(180, 560, fill='black', font="Times 12 bold", text = "Health:{} SP:{} DP:{} Key:{}".format( hp, sp, dp, keyvalue))

    def drawenemy_display(self, sp, dp, hp, key):
        keyvalue = "None"
        if key == True:
            keyvalue = "Keyholder"
        self.canvas.delete(self.enemydisplay_id)
        self.enemydisplay_id = self.canvas.create_text(180, 580, fill='red', font="Times 12 bold", text = "Health:{} SP:{} DP:{} Key:{}".format( hp, sp, dp, keyvalue))

    def display_killed(self):
        self.canvas.delete(self.enemydisplay_id)
        self.enemydisplay_id = self.canvas.create_text(180, 580, fill='black', font="Times 12 bold", text = "Your enemy is dead!")

    def display_blank(self):
        self.canvas.delete(self.enemydisplay_id)

    def display_gameover(self):
        self.canvas.delete(self.hero_id)
        self.canvas.create_text(250, 300, fill='red', font="Times 48 bold", text = "GAME OVER!")
        self.canvas.create_text(250, 380, fill='red', font="Times 20 bold", text = "Press r to restart or Esc to quit")

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

    def draw_boss(self, x, y, hp):
        self.canvas.delete(self.boss_id)
        if hp > 0:
            self.boss_id = self.canvas.create_image(x*50,y*50, anchor=NW, image=self.boss)

    def draw_skeletongroup(self, sklist):

        for i in range(len(sklist)):

                x = sklist[i][0]
                y = sklist[i][1]
                if sklist[i][2] <= 0:
                    self.skeleton_idlist.append('')
                else:
                    self.skeleton_idlist.append(self.canvas.create_image(x*50,y*50, anchor=NW, image=self.skeleton))

                if len(sklist) < len(self.skeleton_idlist):
                    self.canvas.delete(self.skeleton_idlist[0])
                    self.skeleton_idlist = self.skeleton_idlist[1:]

    def launch_screen(self):
        self.root.mainloop()

#    def thing(event):
#            print(event)
