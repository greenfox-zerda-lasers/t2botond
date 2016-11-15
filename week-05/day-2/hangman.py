import guessword
import texts
import random

hidden = []
random = []

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
        self.isrunnung = True
        self.random_item = random.choice(guessword.word_list) #word_list
        self.tries = len(self.random_item)*3
        print( texts.intro['welcome_msg'].format( self.player.name, self.tries))
        for i in random_item:
            hidden.append("*")
        self.gameLoop()
        print("start done")

    def gameLoop(self):
        print("gameLoop done")
        while not self.isrunning == True:
            print( texts.loop['restart_question'] )
            answer = str(input('(Y)es or (N)o?'))
            if self.tries == 0:
                print(text.loop['player_lost'])
                self.isrunning = False
                self.restart()

            else:
                self.tries -= 1
                self.get_guesses()

    def restart(self):
        while not self.isrunning:
                print(texts.loop['restart_question'])
                answer = str(input('(y)es, or (n)o?'))
                if answer.lower() == 'y':
                    self.start()
                elif answer.lower() == 'n':
                    print(texts.loop['see you later'])
                    break
                else: print(texts.loop['false_yn'])

    def charfinder(x, z):
        counter = 0
        for i in x:
            if i == z:
                show.append(counter)
                show.sort()
                print(show)
            counter += 1
        return show

    def show_found():
        for i in show:
            hidden[i] = random_item[i]
        solustring = ''.join(hidden)
        return solustring


    def get_guesses(self):
        guess = input( texts.loop['letter_ask'])
        guessword.charfinder(self.random_item, guess)
        print(guessword.show_found())

player = Player("Botond")
hangman = Game(player)
