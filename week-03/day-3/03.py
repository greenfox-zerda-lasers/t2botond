# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise
class Pirate():
    rum1 = 0

#    def __init__ (self, drink_rum):
#        self.drink_rum = drink_rum

    def drink_rum(self):
        self.rum1 += 1
        return self.rum1

    def hows_goin_mate(self):
        if self.rum1 < 5:
            return "Nothin"
        else:
            return "Arrrr!"

jack = Pirate()

for i in range(7):
    print(jack.drink_rum())
    print(jack.hows_goin_mate())
