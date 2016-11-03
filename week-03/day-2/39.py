names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list
def shortest(i):
    x=i[0]
    print(len(x))
    for z in range(len(i)):
        if len(x) >= len(i[z]):
            x = i[z]
            print(x)
    return x
print(shortest(names))
