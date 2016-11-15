
# Adds a and b, returns as result
def add(a, b):
    c = a + b
    return c

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > c and b > c:
        return b
    else:
        return c

#Returns the median value of a list given as param
def median(pool):
    list = []
    list = sorted(pool)
    if len(list)%2 == 0:
        return (list[int((len(list)-1) / 2)] + list[int(((len(list)-1) / 2)+1)])/2
    else:
        return list[int((len(list) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    if len(char)>1:
        return TypeError
    char = char.lower()
    if char in 'aeiouéáőűöüóí':
        return True
# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    teve2 = []
    for char in teve:
        if is_vovel(char):
            teve2.append(char)
            teve2.append("v")
            teve2.append(char)
        else:
            teve2.append(char)
    return ''.join(teve2)
