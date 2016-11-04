# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has
j = 150
x=0
for i in range(j):
    print((j)*' '+'*'*(i*2+1))
    j-=1
    x+=2
