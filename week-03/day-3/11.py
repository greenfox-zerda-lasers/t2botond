# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has
j = 50
k = j
l = j
x=0
for i in range(j):
    print((j)*' '+'*'*(i*2+1))
    j-=1
    x+=2
x=k*2-1
for i in range(k-2):
    print((i+2)*' '+(x-2)*'*')
    k-=1
    x-=2
if l > 0:
    print(l*' '+'*')
