import view
import model

class Game_play:
    def __init__(self):
        self.screen = view.Draw()
        self.ship = model.Starship()
        for i in range(15):
            self.screen.spaceship(self.ship.starty)
            self.object_model = model.Space_objects()
            self.screen.root.bind('<Down>',self.movedown)
            self.screen.root.bind('<Up>',self.moveup)
            self.object_model.planetoid_model()
            self.screen.planetoid_view(self.object_model.planetoid_model(), self.object_model.planetoid_color(),self.object_model.startvalues() )
            self.object_model = model.Space_objects()
            self.object_model.planetoid_model()
            self.screen.planetoid_view(self.object_model.planetoid_model(), self.object_model.planetoid_color(),self.object_model.startvalues() )
        self.screen.launch_screen()

    def movedown(self, event):
        self.screen.spaceship(self.ship.starshipdown())

    def moveup(self, event):
        self.screen.spaceship(self.ship.starshipup())

test = Game_play()
