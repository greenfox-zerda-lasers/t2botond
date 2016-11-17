class Elevator:
    def __init__(self):
        self.floor = 0
        self.people = True

    def floorup(self):
        if self.floor == 10:
            pass
        else:
            self.floor += 1

    def floordown(self):
        if self.floor == 0:
            pass
        else:
            self.floor -= 1

    def geton(self):
        if self.people == True:
            pass
        else:
            self.people = True
    def getoff(self):
        if self.people == False:
            pass
        else:
            self.people = False
