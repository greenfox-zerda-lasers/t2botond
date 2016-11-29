from tkinter import *
from PIL import ImageTk, Image
import math
import time
import random

class Draw:
    def __init__(self):
        screenwidth = 1000
        screenheight = 500
        self.centerx = screenwidth / 2
        self.centery = screenheight / 2
        self.root = Tk()
        self.canvas = Canvas(self.root, width = screenwidth, height = screenheight, bg = "black")
        self.canvas.pack()
        self.futuramaship = []
        self.exp = []
        self.futuramaship.append(PhotoImage(file = "spaceship.png"))
        self.futuramaship.append(PhotoImage(file = "spaceship1.png"))
        self.futuramaship.append(PhotoImage(file = "spaceship2.png"))
        self.exp.append(PhotoImage(file = "slice_3_3.png"))
        self.exp.append(PhotoImage(file = "slice_3_2.png"))
        self.exp.append(PhotoImage(file = "slice_3_1.png"))
        self.exp.append(PhotoImage(file = "slice_3_0.png"))
        self.exp.append(PhotoImage(file = "slice_2_3.png"))
        self.exp.append(PhotoImage(file = "slice_2_2.png"))
        self.exp.append(PhotoImage(file = "slice_2_1.png"))
        self.exp.append(PhotoImage(file = "slice_2_0.png"))
        self.exp.append(PhotoImage(file = "slice_1_3.png"))
        self.exp.append(PhotoImage(file = "slice_1_2.png"))
        self.exp.append(PhotoImage(file = "slice_1_1.png"))
        self.exp.append(PhotoImage(file = "slice_1_0.png"))
        self.exp.append(PhotoImage(file = "slice_0_3.png"))
        self.exp.append(PhotoImage(file = "slice_0_2.png"))
        self.exp.append(PhotoImage(file = "slice_0_1.png"))
        self.exp.append(PhotoImage(file = "slice_0_0.png"))

        self.collosion = False
        self.height = self.centery
        self.spaceship_id = ''
        self.explosion_id = ''
        self.expcounter = 0

    def spaceship(self, newheight):
        if self.collosion == False:
            self.height = newheight
            self.canvas.delete(self.spaceship_id)
            self.spaceship_id = self.canvas.create_image(100,self.height, anchor=N, image = random.choice(self.futuramaship))

    def explosion(self):
        if self.expcounter / 20 < 15:
            self.canvas.delete(self.explosion_id)
            self.explosion_id = self.canvas.create_image(90,self.height, anchor=N, image =self.exp[int(self.expcounter/20)])
            self.expcounter += 1
            if expcounter / 20 > 10:
                self.canvas.delete(self.spaceship_id)
        else :
            self.canvas.delete(self.explosion_id)
            self.canvas.delete(self.spaceship_id)

    def planetoid_view(self, outline, color, startvalues):

        self.outline = outline
        self.color = color
        self.startvalues = startvalues
        self.outline_show = []
        self.outline_subshow = []
        self.r = 0
        self.onscreen = True
        self.x = self.centerx * 2 +200
        self.y = self.centery + self.startvalues[3]
        self.planetoid_id = ''


        while self.onscreen == True:
            self.maxy = 0
            self.miny = 1000
            self.minx = 0
            self.x -= self.startvalues[0] / 100
            self.y += self.startvalues[1] /100000

            for i in self.outline:
                c = math.sqrt(i[0] ** 2 + i[1] ** 2)
                alfa = math.asin(i[1] / c)
                newy = c * math.sin(alfa + self.r/180)
                newx = c * math.cos(alfa + self.r/180)

                if i[0] > 0:
                    newx = - newx
                    newy = - newy

                self.outline_subshow.append(newx)
                self.outline_subshow.append(newy)
                self.outline_show.append(self.outline_subshow)
                self.outline_subshow = []

            self.canvas.delete(self.planetoid_id)
            self.spaceship(self.height)
            self.planetoid_id = self.canvas.create_polygon(self.outline_show[0][0] + self.x, self.outline_show[0][1] + self.y,
                                                            self.outline_show[1][0] + self.x, self.outline_show[1][1] + self.y,
                                                            self.outline_show[2][0] + self.x, self.outline_show[2][1] + self.y,
                                                            self.outline_show[3][0] + self.x, self.outline_show[3][1] + self.y,
                                                            self.outline_show[4][0] + self.x, self.outline_show[4][1] + self.y,
                                                            self.outline_show[5][0] + self.x, self.outline_show[5][1] + self.y,
                                                            self.outline_show[6][0] + self.x, self.outline_show[6][1] + self.y,
                                                            self.outline_show[7][0] + self.x, self.outline_show[7][1] + self.y,
                                                            self.outline_show[8][0] + self.x, self.outline_show[8][1] + self.y,
                                                            self.outline_show[9][0] + self.x, self.outline_show[9][1] + self.y,
                                                            self.outline_show[10][0] + self.x, self.outline_show[10][1] + self.y,
                                                            self.outline_show[11][0] + self.x, self.outline_show[11][1] + self.y, fill = self.color)
            if self.x < -400 or self.x > 1800 or self.y < -200 or self.y > 1000:
                self.onscreen = False

            self.outline_show = []
            self.crash = []
            self.crash.append(self.canvas.find_overlapping(50, self.height,150, self.height+39))
            try :
                if self.crash[0][1] > 0:
                    self.collosion = True
                    self.explosion()
            except:
                pass
            self.canvas.update()
            self.r += 0.02 * self.startvalues[2]

    def launch_screen(self):
        self.root.mainloop()
