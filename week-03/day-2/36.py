numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list
def res(i):
    j=[]
    x = len(i)-1
    while x!=-1:
        j.append(i[x])
        x-=1
    return j
print(res(numbers))
