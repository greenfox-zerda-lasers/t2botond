# Create a method that returns the five most frequent lottery number in a pretty table format
def five_most_frequent():
    import csv
    f = open('D:/greenfox/Greenfox/t2botond/week-04/day-1/02_pip/lottery/otos.csv')
    content = csv.reader(f, delimiter=";")
    resultlist = []
    i=91
    occurence = 0
    max1=0
    max2=0
    max3=0
    max4=0
    max5=0
    while i > 0:
        i-=1
        resultlist.append(0)
    for row in content:
        resultlist[int(row[len(row)-1])]+=1
        resultlist[int(row[len(row)-2])]+=1
        resultlist[int(row[len(row)-3])]+=1
        resultlist[int(row[len(row)-4])]+=1
        resultlist[int(row[len(row)-5])]+=1
    print(resultlist)
    for i in range(len(resultlist)):
        if resultlist[i] > occurence:
            occurence = resultlist[i]
            print(occurence)
            max1 = i
    occurence=0
    for i in range(len(resultlist)):
        if i == max1:
            max1 = max1
        elif resultlist[i] > occurence:
            occurence = resultlist[i]
            print(occurence)
            max2 = i
    occurence=0
    for i in range(len(resultlist)):
        if i == max1 or i == max2:
            max1 = max1
        elif resultlist[i] > occurence:
            occurence = resultlist[i]
            print(occurence)
            max3 = i
    for i in range(len(resultlist)):
        if i == max1 or i == max2 or i == max3:
            max1 = max1
        elif resultlist[i] > occurence:
            occurence = resultlist[i]
            print(occurence)
            max4 = i
    occurence=0
    for i in range(len(resultlist)):
        if i == max1 or i == max2 or i == max3 or i == max4:
            max1 = max1
        elif resultlist[i] > occurence:
            occurence = resultlist[i]
            print(occurence)
            max5 = i

    print(max1,max2,max3,max4,max5)





five_most_frequent()
