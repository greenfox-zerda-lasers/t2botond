# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.
def counter(filename):
    try:
        with open(filename) as f:
            content = f.readlines()
    except FileNotFoundError:
        return "No such file"
    line = 0
    for i in content:
        line += 1
    return line

#print("Gimme filename!")
#print(counter(input()))
