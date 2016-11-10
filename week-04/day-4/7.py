# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
def xtoy(string):
    if not string:
        return string
    elif string[0] == 'x':
        string = string[0].replace('x','y')+xtoy(string[1:])
        return string
    else :
        return string[0]+xtoy(string[1:])

kkk = 'xsvjxsjijiedijxijsqoixijxjipoxiwuixife'
print(xtoy(kkk))
