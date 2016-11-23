import Tkwander_view
import map_data
import Character

class Game_play:
    def __init__(self):
        self.screenview = Tkwander_view.Draw()
        self.mapdata = map_data.Map()
        self.herodata = Character.Hero()
        self.bossdata = Character.Boss()
        self.skeletondata = Character.Skeletongroup()
        self.screenview.draw_background(self.mapdata.game_field_elements)
        self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
        self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy)
        self.screenview.draw_skeletongroup(self.skeletondata.skeletonlist)
        self.screenview.root.bind('<s>',self.movedown)
        self.screenview.root.bind('<w>',self.moveup)
        self.screenview.root.bind('<a>',self.moveleft)
        self.screenview.root.bind('<d>',self.moveright)
        self.movecounter = 0
        self.screenview.launch_screen()

    def movedown(self, event):
        self.moveenemy()
        self.herodata.hero_move_down()
        self.screenview.draw_hero_front(self.herodata.posx, self.herodata.posy)
    def moveup(self, event):
        self.moveenemy()
        self.herodata.hero_move_up()
        self.screenview.draw_hero_back(self.herodata.posx, self.herodata.posy)
    def moveleft(self, event):
        self.moveenemy()
        self.herodata.hero_move_left()
        self.screenview.draw_hero_left(self.herodata.posx, self.herodata.posy)
    def moveright(self, event):
        self.moveenemy()
        self.herodata.hero_move_right()
        self.screenview.draw_hero_right(self.herodata.posx, self.herodata.posy)

    def moveenemy(self):
        if self.movecounter%2 == 0:
            self.bossdata.boss_move()
            self.screenview.draw_boss(self.bossdata.posx, self.bossdata.posy)
        self.movecounter += 1



test = Game_play()
#test.screenview.canvas.mainloop()
