# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.
def acounter(filename):
    a_number = 0
    charlist = list(filename)
    try:
        f = open('%s.txt' filename , 'r') #          '%s.txt' % filename, "r")
        f.close()
        for i in charlist:
            if i == "a":
                a_number += 1
        print(a_number)

    except:
        print('0')

name = "almafa_alatt"
acounter(name)
