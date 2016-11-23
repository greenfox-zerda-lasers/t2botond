import Tkwander_view

class Game_map:

    def __init__(self):

        self.game_field_elements = wallitems = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                                                [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                                                [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                                                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                                [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                                                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                                                [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                                                [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
                                                [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                                                [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
