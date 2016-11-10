# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def power(n,k):
    if n == 0:
        return 0
    elif k == 0:
        return 1
    else:
        return n*power(n,(k-1))

print(power(2,0))
