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
