# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.
def remover(string2):
    if not string2:
        return string2
    elif string2[0] == 'x':
        return remover(string2[1:])
    else :
        return string2[0] + remover(string2[1:])

print(remover('xsxsxnsnxsixsi'))
