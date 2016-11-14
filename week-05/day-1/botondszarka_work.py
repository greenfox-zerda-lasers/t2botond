def anagramm(stg1, stg2):
    compstg1 = []
    compstg2 = []
    new1 = []
    new2 = []
    compstg1 = stg1.lower()
    compstg2 = stg2.lower()
    compstg1 = sorted(compstg1)
    compstg2 = sorted(compstg2)
    for i in compstg1:
        if i == " ":
            i = ""
        else:
            new1.append(i)
    for i in compstg2:
        if i == " ":
            i = ""
        else:
            new2.append(i)
    if compstg1 == compstg2:
        return True
    else:
        return False

def count_letters(stg3):
    count1 = []
    newcount1 = []
    countdict = {}
    count1 = stg3.lower()
    for i in count1:
        if i.isalnum()!= True:
            i = ""
        elif i.isdigit() == True:
            i = ""
        else:
            newcount1.append(i)
    for i in newcount1:
        countdict[i] = count1.count(i)
    return countdict

print(count_letters("1111111111i.isdigit()")) #aabbakfDDDglgmasvbhh
print(anagramm("321ab c","1c ab23"))
