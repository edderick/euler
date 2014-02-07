#a = 1; b = 2; c = 997
#a = 332; b = 333; c = 335

def is_pythag(a, b, c):
    return a**2 + b**2 == c**2

for c in range(335, 997):
    for a in range(1, 332):
        b = 1000 - c - a
        if b < 0:
            continue
        if is_pythag(a, b, c):
            print "{}**2 * {}**2 = {}**2".format(a,b,c)
            print "{} * {} * {} = {}".format(a,b,c, a*b*c)
