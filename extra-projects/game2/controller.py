import view
import model
import sys
import records

class Game_play:
    def __init__(self):
        self.screen = view.Draw()
        self.ship = model.Starship()
        self.recordchecker = records.Recordhandle()

        while self.screen.collosion == False:
            self.screen.spaceship(self.ship.starty)
            self.object_model = model.Space_objects()
            self.screen.root.bind('<Down>',self.movedown)
            self.screen.root.bind('<Up>',self.moveup)
            self.object_model.planetoid_model(self.screen.distancecounter)
            self.screen.planetoid_view(self.object_model.planetoid_model(self.screen.distancecounter), self.object_model.planetoid_color(),self.object_model.startvalues() )
        if self.screen.distancecounter > self.recordchecker.min_to_board():
            self.recordchecker.write()
            self.recordchecker.compare(self.screen.distancecounter)
        self.screen.show_winners(self.recordchecker.best_current())
        self.gameover()
        self.screen.launch_screen()

    def play(self, event):
        self.screen.root.bind('<space>',self.blank)
        self.screen.root.bind('<Escape>',self.blank)
        self.screen.newgame()
        self.screen.collosion = False
        while self.screen.collosion == False:
            self.screen.spaceship(self.ship.starty)
            self.object_model = model.Space_objects()
            self.screen.root.bind('<Down>',self.movedown)
            self.screen.root.bind('<Up>',self.moveup)
            self.object_model.planetoid_model(self.screen.distancecounter)
            self.screen.planetoid_view(self.object_model.planetoid_model(self.screen.distancecounter), self.object_model.planetoid_color(),self.object_model.startvalues() )
        if self.screen.distancecounter > self.recordchecker.min_to_board():
            self.recordchecker.compare(self.screen.distancecounter)
        self.screen.show_winners(self.recordchecker.best_current())
        self.gameover()
        self.screen.launch_screen()

    def gameover(self):
        self.screen.gameover_display()
        self.screen.root.bind('<space>',self.play)
        self.screen.root.bind('<Escape>',self.quit)

    def quit(self, event):
        sys.exit()

    def movedown(self, event):
        self.screen.spaceship(self.ship.starshipdown())

    def moveup(self, event):
        self.screen.spaceship(self.ship.starshipup())

    def blank(self, blank):
        pass

test = Game_play()
