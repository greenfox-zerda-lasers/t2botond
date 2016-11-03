numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function
def summary(i):
    sum=0
    for x in range(len(i)):
        sum = sum + i[x]
    print(sum)

summary(numbers)
