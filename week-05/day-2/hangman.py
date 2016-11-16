import guessword
import texts
import random

hided = []

class Player:
    def __init__(self, name):
        self.n = name
        self.live = 5

class Game:
    def __init__(self, player):
        self.player = player
        self.isrunning = False
        self.random_item = -1 #'tirand='
        self.tries = 5 #szohossz alapjan szamithato

        print(texts.intro['enter_message'])
        self.player.name = input()
        self.start()

    def start(self):
        self.isrunning = True
        self.random_item = random.choice(guessword.word_list) #word_list
        for i in self.random_item:
            hided.append("*")
        self.hiddenmaker()
        self.tries = len(self.random_item)*1
        print( texts.intro['welcome_msg'].format( self.player.name, self.tries))
        self.gameLoop()
        print("start done")
        print(hidden)

    def hiddenmaker(self):
        hidden = []
        for i in self.random_item:
            hidden.append("*")
        return hidden

    def charfinder(self, x, z):
        counter = 0
        show = []
        for i in x:
            if i == z:
                show.append(counter)
                show.sort()
            counter += 1
        return show

    def show_found(self, x, y):
        show = self.charfinder(x, y)
        hidden = self.hiddenmaker()
        for j in show:
            print(j)
            hidden[j] = x[j]
            hided[j] = x[j]
        return hidden

    def gameLoop(self):
        print("gameLoop running")
        while self.isrunning:
            if self.tries == 0:
                print(texts.loop['player_lost'])
                self.isrunning = False
                self.restart()

            else:
                self.tries -= 1
                self.get_guesses()

    def restart(self):
        self.hiddenmaker()
        for i in hided:
            hided.pop()
        while not self.isrunning:
                print(texts.loop['restart_question'])
                answer = str(input('(y)es, or (n)o?'))
                if answer.lower() == 'y':
                    self.start()
                elif answer.lower() == 'n':
                    print(texts.loop['see you later'])
                    break
                else: print(texts.loop['false_yn'])

    def get_guesses(self):
        guess = input( texts.loop['letter_ask'])
        self.charfinder(self.random_item, guess)
        hidden = (self.show_found(self.random_item, guess))
        for i in hidden:
            win = False
            if i!= "*":
                win = True
            elif win == True:
                print(texts.loop['won'])
                self.restart()
        solustring = ''.join(hidden)
        solustring1 = ''.join(hided)
        print(solustring1)

player = Player("Botond")
hangman = Game(player)
