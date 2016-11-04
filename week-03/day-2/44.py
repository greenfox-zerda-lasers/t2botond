filename = 'alma.txt'
# create a function that reads a file and prints it's
# lines, also it should prepend an 'A' character
# to each line
text = open('alma.txt')

with open('alma.txt') as f:
    lines = f.readlines()

z=0
linesA=[]
for i in range(len(lines)):
    linesA.append(lines[i])
    linesA[i]="A " + linesA[i]
    print(linesA[i])
