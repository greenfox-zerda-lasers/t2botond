import sys
import taskitem

class Todo:
    def run(self):
        if len(sys.argv) == 1:
            print("List all tasks: -l")
            print("Add new task: -a")
            print("Remove task: -r")
            print("Completes a task: -c")

        if len(sys.argv) > 1 :
            self.isrunning = True
            if sys.argv[1] == "-a": #ennek a syarnak a masodik elemebol kell bekerni a fost
                if len(sys.argv) < 4:
                    print("It is a realy long and unaderstandable error message. I just wanted to make you feel the pain while I wrote this ridiculous program. By the way at least one argument is missing")
                else :self.stupidity = "-a"
            if sys.argv[1] == "-l": #ennek a syarnak a masodik elemebol kell bekerni a fost
                self.stupidity = "-l"
            if sys.argv[1] == "-c": #ennek a syarnak a masodik elemebol kell bekerni a fost
                self.stupidity = "-c"
            if sys.argv[1] == "-r": #ennek a syarnak a masodik elemebol kell bekerni a fost
                self.stupidity = "-r"


            if self.stupidity == "-l":
                f = open("fajl", "r")
                self.showlist = []
                linenumbering = 0
                for i in f.readlines():
                    self.showlist.append(i)
                    print(linenumbering,i)
                    linenumbering += 1
                f.close()
            if self.stupidity == "-a":
                self.task = sys.argv[2]
                if sys.argv[3] == '1':
                    self.state = True
                    self.newitem = taskitem.Item(self.state, self.task)
                elif sys.argv[3] == '0':
                    self.state = False
                    self.newitem = taskitem.Item(self.state, self.task)
            if self.stupidity == "-r":
                item = sys.argv[2]
                taskitem.Item.delete(self, item)  #remove method call
            if self.stupidity == "-c":
                item = sys.argv[2]
                taskitem.Item.changestate(self, item)
#            if self.decision !="-l" or self.decision !="-a" or self.decision !="-r" or self.decision !="-c" or self.decision !="False" or self.decision !="True" or self.decision !="":
#                print("Command not valid, retry!")

start = Todo()
start.run()
#sys.argv
