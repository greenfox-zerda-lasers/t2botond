numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens
def removeodd(i):
    j=[]
    for index in range(len(i)):
        if i[index] % 2 == 0 :
            j.append(i[index])
    return j
print(numbers)
print(removeodd(numbers))
