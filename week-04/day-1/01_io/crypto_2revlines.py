# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    linelist = f.readlines()
    result = ''
    for line in linelist:
        charnumber = len(line)
        while charnumber>0:
            charnumber-=1
            result+= line[charnumber]
    return result
    close(file_name)
print(decrypt('D:/greenfox/Greenfox/t2botond/week-04/day-1/01_io/texts/reversed_zen_lines.txt'))
