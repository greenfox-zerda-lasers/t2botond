# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    coded = f.readlines()
    newtext = ''
    for line in coded:
        newtext+="\n"
        for i in line:
            if i == " " :
                newtext+=" "
            else:
                char=ord(i)
                char-=1
                newchar=chr(char)
                newtext+=newchar
    return newtext
    close(file_name)
print(decrypt('D:/greenfox/Greenfox/t2botond/week-04/day-1/01_io/texts/encoded_zen_lines.txt'))
