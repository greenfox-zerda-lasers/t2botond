from tkinter import*
import sys

class Recordhandle:


    def compare(self, distance):
        self.distance = distance
        self.changer = []
        self.newrecord = False
        f = open("bests.txt", "r")
        lines = f.readlines()

        for i in range(len(lines)):
            self.line = lines[i].split(';')

            if int(self.line[0]) >= self.distance:
                self.changer.append(lines[i])

            else:
                if self.newrecord == False:
                    self.changer.append(str(self.distance)+"\n")
                    self.changer.append(self.recordername)
                    self.newrecord = True
                    self.changer.append(lines[i])
                else:
                    if i < len(lines)-1:
                        self.changer.append(lines[i])
        f.close()

    def best_current(self):
            self.current = []
            f = open("bests.txt", "r")
            lines = f.readlines()

            for i in range(len(lines)):
                self.line = lines[i].split(';')
                self.current.append(self.line)

            f.close()
            return self.current

    def min_to_board(self):
            self.minboard = 0
            self.line = []
            f = open("bests.txt", "r")
            lines = f.readlines()
            self.list = lines
            self.line = lines[len(lines)-1].split(";")
            self.minboard =int(self.line[0])
            f.close()
            return self.minboard

    def write(self):
            self.master = Tk()
            self.text = StringVar()
            Label(self.master, text="You achieved top five score! Type your name and press <Enter>:").pack()
            self.e1 = Entry(self.master, textvariable = self.text)
            self.e1.pack()
            self.e1.bind('<Return>',self.submit)
            self.master.mainloop()


    def submit(self, event):
            self.recordername = self.e1.get()
            print(self.recordername)
        #    try:
            self.master.destroy()
        #    except:
            #    self.compare(self.distance)
