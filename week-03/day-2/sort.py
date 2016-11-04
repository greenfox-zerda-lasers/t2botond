def bubble_sort(list):
    ready=False
    while ready == False:
        ready=True
        for i in range(len(list)-1):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                ready=False
    return list
print(bubble_sort([3,9,4,5,2,1]))
