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

    def track(self, track):
        self.track = track
        print("got track")

    def isvalidstep(self, a, b):
    #    fieldlist = []
    #    fieldlist = self.track
    #    print(fieldlist)
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
        self.skcheck = []
        for j in range(self.groupsize):
            self.skeletonlist.append([])
        i = 0
        while i < len(self.skeletonlist):
                x = random.randrange(10)
                y = random.randrange(10)
            #    print(x, y)
                if self.isvalidstep(x, y) == True:
                    self.skeletonlist[i].append(x) #posx
                    self.skeletonlist[i].append(y) #psoy
                    self.skeletonlist[i].append(2 * self.level * random.randint(1, 6)) #hp Harams torlendo
                    self.skeletonlist[i].append(self.level * 2 * random.randint(1, 6)) #dp
                    self.skeletonlist[i].append(self.level * random.randint(1, 6))  #sp
                    if i == 0:
                        self.skeletonlist[i].append(True)
                    else:
                        self.skeletonlist[i].append(False)
                    i += 1

    def individual_move(self):
        j = 0
        while j < len(self.skeletonlist):
            self.posx = self.skeletonlist[j][0]
            self.posy = self.skeletonlist[j][1]
            self.move()
            self.skeletonlist[j][0] = self.posx
            self.skeletonlist[j][1] = self.posy
            j += 1

    def skeletonfight(self):
        return self.skeletonlist

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.posx = 0
        self.posy = 0
        self.hp = 20 + 3 * random.randint(1, 6)
        self.dp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)
#        self.level = 1
        self.haskey = False

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
        self.hp = 20 + 3 * random.randint(1, 6)
        self.dp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)
        self.level = 1
        self.haskey = False
#Monster Lvl x (if boss)
#HP: 2 * x * d6 (+d6)
#DP: x/2 * d6 (+d6/2)
#SP: x * d6 (+x)
