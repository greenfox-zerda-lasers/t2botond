# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f=open(file_name)
    linelist = f.readlines()
    result = ''
    for line in linelist:
        for i, item in enumerate(line):
            if i%2 == 0:
                result+= item
    return result
    close(file_name)
print(decrypt('D:/greenfox/Greenfox/t2botond/week-04/day-1/01_io/texts/duplicated_chars.txt'))
