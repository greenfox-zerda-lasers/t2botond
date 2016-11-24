import Tkwander_view
import map_data
import random

class Character:
    def __init__(self):
            self.hp = 10
            self.dp = 10
            self.sp = 10
            self.level = 1
            self.haskey = False
            self.visible = True

    def isvalidstep(self, a, b):
        if  b >= 0 and b <= 10 and a >= 0 and a <= 9:
            if map_data.Map.game_field_elements[b][a] == 0:
                return True
        else :
                return False

    def move(self):
        previous = 0
        a = random.randrange(4)
        step = False
        while step == False:
            if a == previous:
                a = random.randrange(4)
                a = previous
            if a == 0:
                if self.isvalidstep(self.posx+1, self.posy) == True:
                    self.posx += 1
                    step = True
                else: a +=1
            elif a == 1:
                if self.isvalidstep(self.posx-1, self.posy) == True:
                    self.posx -= 1
                    step = True
                else: a +=1
            elif a == 2:
                if self.isvalidstep(self.posx, self.posy+1) == True:
                    self.posy += 1
                    step = True
                else: a +=1
            elif a == 3:
                if self.isvalidstep(self.posx, self.posy-1) == True:
                    self.posy -= 1
                    step = True
                else: a = 0

class Skeletongroup(Character):
    def __init__(self):
        super().__init__()
        self.groupsize = random.randrange(3, 7, 1)
        self.skeletonlist = []
        for j in range(self.groupsize):
            self.skeletonlist.append([])
        i = 0
        while i < len(self.skeletonlist):
                x = random.randrange(10)
                y = random.randrange(10)
                print(x, y)
                if self.isvalidstep(x, y) == True:
                    self.skeletonlist[i].append(x)
                    self.skeletonlist[i].append(y)
                    i += 1
    def individual_move(self):
        j = 0
        while j < len(self.skeletonlist):
            print(self.skeletonlist[j])
            self.posx = self.skeletonlist[j][0]
            self.posy = self.skeletonlist[j][1]
            self.move()
            self.skeletonlist[j][0] = self.posx
            self.skeletonlist[j][1] = self.posy
            j += 1

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.posx = 0
        self.posy = 0

    def hero_move_down(self):
        if self.isvalidstep(self.posx, (self.posy+1)) == True:
            self.posy += 1

    def hero_move_up(self):
        if self.isvalidstep(self.posx, (self.posy-1)) == True:
            self.posy -= 1

    def hero_move_left(self):
        if self.isvalidstep(self.posx-1, self.posy) == True:
            self.posx -= 1

    def hero_move_right(self):
        if self.isvalidstep(self.posx+1, self.posy) == True:
            self.posx += 1

class Boss(Character):
    def __init__(self):
        super().__init__()
        self.posx = 6
        self.posy = 0
