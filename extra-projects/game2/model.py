import math
import random

class Starship:
    def __init__(self):
        self.starty = 250

    def starshipdown(self):
        self.starty += 18
        if self.starty > 480 :
            self.starty = 470
        return self.starty

    def starshipup(self):
        self.starty -= 18
        if self.starty < 0 :
            self.starty = 0
        return self.starty


class Space_objects:

    def planetoid_model(self, increment):
        self.increment = increment / 3000
        self.planetoid_outlinelist = []
        for i in range(0, 360, 30):
            sublist = []
            size = random.randint(100, 200) + self.increment
            xcoord = int(size * math.cos(math.radians(i)) + random.randint(1, 35))
            sublist.append(xcoord)
            ycoord = int(size * math.sin(math.radians(i)) + random.randint(1, 35))
            if xcoord < 0:
                ycoord = -ycoord
            sublist.append(ycoord)
            self.planetoid_outlinelist.append(sublist)
        self.planetoid_speed = []
        return self.planetoid_outlinelist

    def planetoid_color(self):
            colorlist = ["#444444","#666666","#121212","#222222","#121212","#1C1C1C", "#262626", "#151515"]
            self.planetoid_color = random.choice(colorlist)
            return self.planetoid_color

    def startvalues(self):
        self.planetoid_startvalues = []
        self.planetoid_startvalues.append(random.randint(50, 70)) # x direction speed
        self.planetoid_startvalues.append(random.randint(-2500, 2500)) # y direction speed
        self.rotation = random.randint(-15, 15)
        if self.rotation == 0:
            self.rotation = 3
        self.planetoid_startvalues.append(self.rotation) #rotation speed
        self.planetoid_startvalues.append(random.randint(-200, 200)) #start y value
        return self.planetoid_startvalues
