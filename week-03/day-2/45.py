filename = 'alma.txt'
# Write the numbers from 1 to 10 to the file stored in filename
text = open('alma.txt')

with open('alma.txt','a') as f:
#   lines = f.readlines()
#    f.write()
    for i in range(10):
        f.write(str(i))
        f.write('\n')
