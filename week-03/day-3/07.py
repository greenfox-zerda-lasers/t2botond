# create a function that takes a list and returns a new list with all the elements doubled
class Doublelist():

    def add(self, list):
        self.list = list

    def size(self):
        j=0
        for i in self.list:
            j+=1
        return j

    def double(self):
        doublelist = []
        i = 0
        while i < self.size():
            doublelist+= [self.list[i]*2]
            i+= 1
        return doublelist

items = (1,2,3,4,5,6,7,8,9)
first = Doublelist()
first.add(items)
print(first.double())
