def search(list, x):
    pos=0
    for i in range(len(list)):
        if list[i] == x:
            pos = i
    if pos==0:
            print(-1)
    else: return pos

print(search([4,53,2,4,6,4], 6))
