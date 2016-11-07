# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    linelist = f.readlines()
    ordercounter = len(linelist)
    newtext =''
    while ordercounter > 0:
        ordercounter-=1
        newtext+= linelist[ordercounter]
    return newtext
    close(file_name)
print(decrypt('D:/greenfox/Greenfox/t2botond/week-04/day-1/01_io/texts/reversed_zen_order.txt'))
