numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)
def minimum(i):
    min=i[0]
    for j in range(len(i)):
        if i[j] < min :
            min = i[j]
    return min
print(minimum(numbers))
