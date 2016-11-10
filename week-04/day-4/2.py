# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n
def extrasum(x):
    if x == 1:
        return 1
    else:
        x = x +(x-1)
        return x
print(extrasum(6))
