import Tkwander_view
import map_data
import Character
import random
import sys

class Game_play:
    def __init__(self):
        self.screenview = Tkwander_view.Draw()
        self.mapdata = map_data.Map()
    #    self.herodata = Character.Hero()
    #    self.bossdata = Character.Boss()
    #    self.skeletondata = Character.Skeletongroup()
        self.screenview.draw_background(self.mapdata.game_field_elements)
    #    self.screenview.draw_display(self.herodata.sp, self.herodata.dp, self.herodata.hp, self.herodata.haskey)
    #    self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
    #    self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy, self.bossdata.hp)
    #    self.screenview.draw_skeletongroup(self.skeletondata.skeletonlist)
    #    self.screenview.root.bind('<s>',self.movedown)
    #    self.screenview.root.bind('<w>',self.moveup)
    #    self.screenview.root.bind('<a>',self.moveleft)
    #    self.screenview.root.bind('<d>',self.moveright)
    #    self.screenview.root.bind('<space>',self.checkfight)
    #    self.screenview.level_display(self.herodata.level)
    #    self.movecounter = 0
        self.screenview.launch_screen()

    def next_level(self, event):
        self.leveladder = self.herodata.level
        self.mapdata = map_data.Map()
#        self.track = self.mapdata.game_fields()
#        self.screenview.draw_background(self.track)
#        self.chara = Character.Character()
#        self.chara.track(self.track)
        self.screenview.draw_background(self.mapdata.game_field_elements)
        self.herodata = Character.Hero()
        self.herodata.level = self.leveladder + 1
        self.bossdata = Character.Boss()
        self.bossdata.level = self.leveladder +1
        self.skeletondata = Character.Skeletongroup()
        self.skeletondata.level = self.leveladder* +1
        self.screenview.draw_display(self.herodata.sp, self.herodata.dp, self.herodata.hp, self.herodata.haskey)
        self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
        self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy, self.bossdata.hp)
        self.screenview.draw_skeletongroup(self.skeletondata.skeletonlist)
        self.screenview.root.bind('<s>',self.movedown)
        self.screenview.root.bind('<w>',self.moveup)
        self.screenview.root.bind('<a>',self.moveleft)
        self.screenview.root.bind('<d>',self.moveright)
        self.screenview.root.bind('<space>',self.checkfight)
        self.screenview.root.bind('<c>',self.blank)
        self.bossdata.level += 1
        self.skeletondata.level += 1
        self.screenview.level_display(self.herodata.level)
        self.screenview.display_blank()
        self.screenview.draw_display(self.herodata.sp, self.herodata.dp, self.herodata.hp, self.herodata.haskey)

        self.movecounter = 0

    def new_game(self, event):
        self.mapdata = map_data.Map()
        self.herodata = Character.Hero()
        self.bossdata = Character.Boss()
        self.skeletondata = Character.Skeletongroup()
        self.screenview.draw_background(self.mapdata.game_field_elements)
        self.screenview.draw_display(self.herodata.sp, self.herodata.dp, self.herodata.hp, self.herodata.haskey)
        self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
        self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy, self.bossdata.hp)
        self.screenview.draw_skeletongroup(self.skeletondata.skeletonlist)
        self.screenview.display_blank()
        self.screenview.level_display(self.herodata.level)
        self.screenview.root.bind('<s>',self.movedown)
        self.screenview.root.bind('<w>',self.moveup)
        self.screenview.root.bind('<a>',self.moveleft)
        self.screenview.root.bind('<d>',self.moveright)
        self.screenview.root.bind('<space>',self.checkfight)
        self.movecounter = 0

    def movedown(self, event):
        self.moveenemy()
        self.herodata.hero_move_down()
        self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
        self.screenview.root.bind('<space>',self.checkfight)

    def moveup(self, event):
        self.moveenemy()
        self.herodata.hero_move_up()
        self.screenview.draw_hero_back(self.herodata.posx, self.herodata.posy)
        self.screenview.root.bind('<space>',self.checkfight)


    def moveleft(self, event):
        self.moveenemy()
        self.herodata.hero_move_left()
        self.screenview.draw_hero_left(self.herodata.posx, self.herodata.posy)
        self.screenview.root.bind('<space>',self.checkfight)


    def moveright(self, event):
        self.moveenemy()
        self.herodata.hero_move_right()
        self.screenview.draw_hero_right(self.herodata.posx, self.herodata.posy)
        self.screenview.root.bind('<space>',self.checkfight)


    def moveenemy(self):
        if self.movecounter%2 == 0:
            self.skeletondata.individual_move()
            self.screenview.draw_skeletongroup(self.skeletondata.skeletonlist)
            self.bossdata.move()
            self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy, self.bossdata.hp)
        self.movecounter += 1

    def quitgame(self, event):
        sys.exit()

    def blank(self, event):
        pass

    def checkfight(self, eventsss):
        if self.herodata.hp > 30:
            self.herodata.hp = 30
        if self.herodata.posx == self.bossdata.posx and self.herodata.posy == self.bossdata.posy:
            svhero = self.herodata.sp + 2 * random.randint(1, 6)
            svboss = self.bossdata.sp + 2 * random.randint(1, 6)

            if svhero > self.bossdata.dp:
                self.bossdata.hp -= (svhero - self.bossdata.dp)

            if svboss > self.bossdata.dp and self.bossdata.hp > 0:
                self.herodata.hp -= (svboss - self.herodata.dp)

                if self.herodata.hp <= 0:
                    self.screenview.display_gameover()
                    self.screenview.root.bind('<Escape>',self.quitgame)
                    self.screenview.root.bind('<r>', self.new_game)
                    self.screenview.root.bind('<s>',self.blank)
                    self.screenview.root.bind('<w>',self.blank)
                    self.screenview.root.bind('<a>',self.blank)
                    self.screenview.root.bind('<d>',self.blank)

            if self.bossdata.hp >= 0:
                self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy, self.bossdata.hp)
                self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
            else:
                self.screenview.display_killed()
                self.herodata.dp += random.randint(1, 6)
                self.herodata.hp += random.randint(1, 6)
                if self.herodata.hp > 30:
                    self.herodata.hp = 30
                self.herodata.sp += random.randint(1, 6)
                self.screenview.root.bind('<space>', self.blank)

            self.screenview.draw_display(self.herodata.sp, self.herodata.dp, self.herodata.hp, self.herodata.haskey)

            if self.bossdata.hp > 0:
                self.screenview.drawenemy_display(self.bossdata.sp, self.bossdata.dp, self.bossdata.hp, self.bossdata.haskey)


        for i in self.skeletondata.skeletonlist:
            if self.herodata.hp > 30:
                self.herodata.hp = 30
            if i[0] == self.herodata.posx and i[1] == self.herodata.posy:
                svhero = self.herodata.sp + 2 * random.randint(1, 6)
                svskeleton = i[4] + 2 * random.randint(1, 6)

                if svhero > i[3]:
                    i[2] -= (svhero - i[3])

                if svskeleton > i[3] and i[2] > 0:
                    self.herodata.hp -= (svskeleton - self.herodata.dp)

                    if self.herodata.hp <= 0:
                        self.screenview.display_gameover()
                        self.screenview.root.bind('<Escape>',self.quitgame)
                        self.screenview.root.bind('<r>', self.new_game)
                        self.screenview.root.bind('<s>',self.blank)
                        self.screenview.root.bind('<w>',self.blank)
                        self.screenview.root.bind('<a>',self.blank)
                        self.screenview.root.bind('<d>',self.blank)

                if i[2] <= 0:
                    self.screenview.display_killed()
                    self.herodata.dp += random.randint(1, 6)
                    self.herodata.hp += random.randint(1, 6)
                    if self.herodata.hp > 30:
                        self.herodata.hp = 30
                    self.herodata.sp += random.randint(1, 6)
                    self.screenview.root.bind('<space>', self.blank)

                    if i[5] == True:
                        self.herodata.haskey = True
                        self.screenview.root.bind('<c>',self.next_level)
                        self.screenview.display_levelup()
                        self.screenview.root.bind('<s>',self.blank)
                        self.screenview.root.bind('<w>',self.blank)
                        self.screenview.root.bind('<a>',self.blank)
                        self.screenview.root.bind('<d>',self.blank)
                    self.screenview.draw_skeletongroup(self.skeletondata.skeletonlist)

                self.screenview.draw_display(self.herodata.sp, self.herodata.dp, self.herodata.hp, self.herodata.haskey)

                if i[2] > 0:
                    self.screenview.drawenemy_display(i[4], i[3], i[2], i[5])
        if self.herodata.hp > 30:
            self.herodata.hp = 30
test = Game_play()
#test.screenview.canvas.mainloop()
