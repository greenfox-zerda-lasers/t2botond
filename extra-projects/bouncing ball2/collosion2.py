import random

#   COLLOSIONS OF THE BALL
def colltop(vy, vyincrement):
    vy = -(vy + vyincrement)
    return vy
def collbottom(vy, vyincrement):
    vy = -(vy + vyincrement)
    return vy
def collleft(vx):
    vx = -vx
    return vx
def collright(vx):
    vx = -vx
    return vx

#   COLOR CHANGES OF THE BALL  '#'+''

def generate_color():
    r = lambda: random.randint(0,255)
    color =('#%02X%02X%02X' % (r(),r(),r()))
    return color
