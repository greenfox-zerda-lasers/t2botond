# Create a method that returns the five most frequent lottery number in a pretty table format
def five_most_frequent():
    import csv
    f = open('D:/greenfox/Greenfox/t2botond/week-04/day-1/02_pip/lottery/otos.csv')
    content = csv.reader(f, delimiter=";")
    resultlist = []
    stat = []
    i=91
    occurence = 0
    max1=1
    index=0
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
    #print(resultlist)
    while sum(resultlist) > 0:
        i=90
        while i > 0:
            if resultlist[i]>occurence:
                max1 = i
                occurence=resultlist[i]
                resultlist[i]=0
            if i == 1:
                stat.append(max1)
            i-=1
            print(max1)
    print(stat)
five_most_frequent()
