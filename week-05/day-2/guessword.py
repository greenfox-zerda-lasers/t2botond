import random

searchchar = 'o'
searchchar2 = 'r'
word_list = ["from","battle"]#,"ride","blazing","sky","chain","fate","hold","fiery","stride","again","when","die","high","mighty","alone","king","whirlwinds","providence","brought","crown","ring"
#"covered","blood","heroes","enemies","knowing"]
show = []
#hidden = []
random_item = []

#def starttba

#for i in random_item:
#    hidden.append("*")

#def charfinder(x, z):
#    counter = 0
#    for i in x:
#        if i == z:
#            show.append(counter)
#            show.sort()
#            print(show)
#        counter += 1
#    return show

def show_found():
    for i in show:
        hidden[i] = random_item[i]
    solustring = ''.join(hidden)
    return solustring

#test resy
#print(charfinder(random_item, searchchar2))
#print(charfinder(random_item, searchchar))
#show_found()
#solustring = ''.join(hidden)
#print(hidden)
#print(solustring)
