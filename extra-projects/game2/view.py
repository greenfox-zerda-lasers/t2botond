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
        self.exp.append(PhotoImage(file = "r11.png"))
        self.exp.append(PhotoImage(file = "r12.png"))
        self.exp.append(PhotoImage(file = "r13.png"))
        self.exp.append(PhotoImage(file = "r14.png"))
        self.exp.append(PhotoImage(file = "r15.png"))
        self.exp.append(PhotoImage(file = "r16.png"))
        self.exp.append(PhotoImage(file = "r17.png"))
        self.exp.append(PhotoImage(file = "r18.png"))
        self.exp.append(PhotoImage(file = "r21.png"))
        self.exp.append(PhotoImage(file = "r22.png"))
        self.exp.append(PhotoImage(file = "r23.png"))
        self.exp.append(PhotoImage(file = "r24.png"))
        self.exp.append(PhotoImage(file = "r25.png"))
        self.exp.append(PhotoImage(file = "r26.png"))
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
        if self.expcounter < 13:
            self.canvas.delete(self.explosion_id)
            self.explosion_id = self.canvas.create_image(100,self.height, anchor=N, image =self.exp[self.expcounter])
            self.expcounter += 1
            time.sleep(0.1)
    #    self.canvas.delete(self.explosion_id)

    def planetoid_view(self, outline, color, startvalues):

        self.outline = outline
        self.color = color
        self.startvalues = startvalues
        self.outline_show = []
        self.outline_subshow = []
        r = 0
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
                newy = c * math.sin(alfa + r/180)
                newx = c * math.cos(alfa + r/180)

                if i[0] > 0:
                    newx = - newx
                    newy = - newy

                if newy + self.y > self.maxy:
                    self.maxy = newy + self.y
                if newy + self.y < self.miny:
                    self.miny = newy + self.y
                if self.minx < self.x - newx and newx + self.x > 0 :
                    self.minx = newx+self.x

                self.outline_subshow.append(newx)
                self.outline_subshow.append(newy)
                self.outline_show.append(self.outline_subshow)
                self.outline_subshow = []


            if self.height > self.miny and self.height < self.maxy and self.minx < 150:  #collosiondetection
                print("Collosion")
                self.explosion()
                self.collosion = True
            #    if self.minx < 200:
            #        print("minx")

            else: print("all right!")
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
            if self.x < -200 or self.x > 1800 or self.y < -200 or self.y > 1000:
                self.onscreen = False
                print("out of screen")
            self.outline_show = []
            time.sleep(0.005)

            self.canvas.update()
            r += 0.02 * self.startvalues[2]

    def launch_screen(self):
        self.root.mainloop()
