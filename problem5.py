top = 20

x = 1

for i in range(1, top + 1):
    x *= i

def divides_by_all(x, top):
    for i in range(1, top + 1):
        if x % i != 0:
            return False
    return True

for i in reversed(range(2, top + 1)):
    if divides_by_all(x / i, top):
        x = x / i


print x
