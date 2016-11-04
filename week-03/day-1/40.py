numbers=(1,2,3,4,5,6,7,8,9)
odd=0
even=0
for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
