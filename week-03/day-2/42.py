filename = 'alma.txt'
# write a function that reads a file and prints how many
# lines and characters in it

text = open('alma.txt')

with open('alma.txt') as f:
    lines = f.readlines()

print(len(lines))
z=0
for i in range(len(lines)):
    z=z+len(lines[i])
    print(z)
