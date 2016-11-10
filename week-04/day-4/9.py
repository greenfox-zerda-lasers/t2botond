# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
def star(q):
    if not q:
        return q
    else:
        if q[1:] == '':
            return q
        print(q[0])
        return q[0] + '*' + star(q[1:])


print(star('cjdwci'))
