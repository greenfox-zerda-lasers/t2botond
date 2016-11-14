def colltop(vy, t, g):
    vymod = -(vy)
    return vymod
def collbottom(vy, t, g):
    vy = -(vy + (g/2)*t**2)
    return vy
def collleft(vx):
    vx = -vx
    return vx
def collright(vx):
    vx = -vx
    return vx
