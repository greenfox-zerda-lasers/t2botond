# create a function that takes a list and returns a new list that is reversed

class Reverselist():

    def add(self, list):
        self.list = list

    def size(self):
        j=0
        for i in self.list:
            j+=1
        return j

    def reverse(self):
        revlist = []
        length = self.size()
        print(length)
        i = 0
        while i < self.size():
            revlist+= [self.list[length-1]]
            length-= 1
            i+= 1
        return revlist
items = (1,2,3,4,5,6,7,8,9)
first = Reverselist()
first.add(items)
print(first.reverse())
