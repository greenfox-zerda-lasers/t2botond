# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).
def bunny(x):
    if x == 1:
        return 2
    else:
        return 2 + bunny(x-1)

print(bunny(11))