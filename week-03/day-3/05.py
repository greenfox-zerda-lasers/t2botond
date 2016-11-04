# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

 #please don`t use the built in methods

class Stack():
    ellist = []

    def push(self, element):
        self.ellist += [element]

    def size(self):
        j=0
        for i in self.ellist:
            j+=1
        return j

    def pop(self):
        sublist=[]
        i = 0
        while i < self.size()-1:
            sublist += [self.ellist[i]]
            i+=1
    #        print(self.ellist)
    #        print(sublist)
        self.ellist = sublist
        return sublist

elso = Stack()
elso.push(1)
elso.push(2)
elso.push(3)
elso.push(4)
print(elso.size())
elso.pop()
print(elso.size())
