import random

def bogo(s, res):
    i = 0
    while s != res:
        s = "".join(random.sample(s, len(s)))
        i += 1
    return i

print str(bogo("lolHe","Hello")) + " iterations"
