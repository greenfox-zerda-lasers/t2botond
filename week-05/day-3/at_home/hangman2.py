
import texts
import words
import random
import sys

class Game:

    def __init__(self):
        self.newgame()

    def newgame(self):
        self.starlist = []
        self.solved = 0
        print(texts.new_game["name"])
        self.name = "Tadam" #input()
        self.chosed = random.choice(words.word_list)
        print(texts.game["length"].format(len(self.chosed)))
        self.lives = len(self.chosed)*2
        for i in self.chosed:
            self.starlist.append("*")
        self.guess()

    def guess(self):
        print(texts.game["guess"])
        self.letter = input()
        self.lives -= 1
        x = 0
        print(texts.game["live"].format(self.lives))
        for i in self.chosed:
            if self.letter == i:
                print(texts.game["hit"])
                print(texts.game["live"].format( self.lives))
                self.starlist[x] = self.letter
                self.solved += 1
            x += 1
        solustring = ''.join(self.starlist)
        print(solustring)
        if self.solved == len(self.chosed):
            print(texts.end["win"])
            self.playagain()
        elif self.lives == 0:
            self.die()
        else:
            self.guess()

    def die(self):
        print(texts.end["die"].format(self.chosed))
        self.playagain()

    def playagain(self):
        print(texts.end["playagain"])
        answer = input()
        if answer == "y":
            self.newgame()
        elif answer == "n":
            sys.exit()
        else:
            print(texts.end["what"])
            self.playagain()

game1 = Game()
