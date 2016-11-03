# create a function that returns it's input factorial
def fact(i):
    j=1
    for k in range(1, i+1):
        j=j*k
    return j
fact(4)
print(fact(66))
