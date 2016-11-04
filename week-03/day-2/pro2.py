def union(list1, list2):
    newlist=[]
    for i in list1:
        if i not in newlist:
            newlist.append(i)
    for i in list2:
        if i not in newlist:
            newlist.append(i)
    return newlist
print(union([4,5,7], [4,1,7]))
