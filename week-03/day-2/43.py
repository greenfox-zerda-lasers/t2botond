filename = 'alma.txt'
# create a function that prints the content of the
# file given in the input

text = open('alma.txt')

with open('alma.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    print(lines[i])
