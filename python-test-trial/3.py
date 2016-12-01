# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume
class Cuboid:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSurface(self):
        return print(2 * (self.a * self.b + self.b * self.c + self.a * self.c))

    def getVolume(self):
        return print(self.a*self.b*self.c)

newcube = Cuboid(1, 2, 3)
newcube.getsurface()
newcube.getvolume()
