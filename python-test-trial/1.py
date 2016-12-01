# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.
def doubler(inputlist):
    numlist = inputlist
    items = len(numlist)
    i = 0
    while items >  0:
        numlist.append(numlist[i]*2)
        items -= 1
        i += 1
    numlist = numlist[6:]
    return print(numlist)

try:
    inputlist = [1, 2, 3, 4, 7, 6]
    doubler(inputlist)
except NameError:
    print("Oops, try it with numbers please.")
