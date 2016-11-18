
class Item:
    def __init__(self, state, task):
        self.state = state
        self.task = task
        f = open("fajl", "a")
        f.writelines(str(self.task)+";"+str(self.state))# Valami itt nem jo ay irast meg kell neyni
#        f.write(";")
#        if self.state == "True":
#            f.write(str(self.state))
#        else:
#            f.write("False")
        f.write('\n')
        f.close()

    def changestate(self, item):
        f = open("fajl", "r")
        self.changelist = []
        self.item = item
        linenumbering = 0
        self.string = []
        self.value = ""
        lines = f.readlines()
        for i in lines:
            self.changelist.append(i)
            #print(linenumbering,i)
            linenumbering += 1
        f.close()
        #print("Add number of line you want to delete:")
        #print("For cancel press c")
        #answer = input()
        l = ''
    #    print(self.changelist)
    #    print(self.item)
        for j in self.changelist[int(self.item)]:
            if j == ";":
                break
            else:
                self.string.append(j)
        for k in self.changelist[int(self.item)]:
            if k == "T" and l == ';':
                self.value = "False"
            elif k == "F" and l == ';':
                self.value = "True"
            l = k
    #        print(self.value)
    #        print(self.string)
        try:
            if int(item) <= linenumbering-1 or int(item) > 0:
        #        print(self.string)1
                #print("lefut")
                self.changelist[int(item)] = ''.join(self.string) + ";" + self.value
                #print(self.dellist)
                f=open('fajl', 'w')
                for i in self.changelist:
                    f.writelines(i)
                f.close()


            elif int(item) > linenumbering-1 or int(item) < 0:
                print("Oops! No such list item!")
        except ValueError:
            print( "Oops!  That was no valid number.  Try again...")


    def addtask(cont):
        self.content = cont

    def delete(self, item):
        f = open("fajl", "r")
        self.dellist = []
        linenumbering = 0
        for i in f.readlines():
            self.dellist.append(i)
            #print(linenumbering,i)
            linenumbering += 1
        f.close()
        #print("Add number of line you want to delete:")
        #print("For cancel press c")
        #answer = input()
        try:
            if int(item) <= linenumbering-1 and int(item) > 0:
                self.dellist[int(item)] = ""
                #print(self.dellist)
                f=open('fajl', 'w')
                for i in self.dellist:
                    f.writelines(i)
                f.close()


            elif int(item) > linenumbering-1 or int(item) <= 0:
                print("Oops! No such list item!")
        except ValueError:
            print( "Oops!  That was no valid number.  Try again...")
