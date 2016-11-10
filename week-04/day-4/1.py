# 1. write a recursive function
# that takes one parameter: n
# and counts down from n
def countdown(x):
    if x == 1:
        print(1)
    else:
        print(x)
        x-= 1
        countdown(x)
countdown(10)
