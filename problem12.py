import math
top = 20

# Generate some primes
l = [True for i in range(0, top)]

l[0] = False
l[1] = False

end = int(math.sqrt(top))

for i in range(2, end + 1):
    if l[i]:
        for j in range(2, int(top / i) + 1):
            if j * i >= top:
                continue
            l[j * i] = False

primes = [i for i, p in enumerate(l) if p]

def num_divisors(x):
    n = 1
    for i in primes:
        b = 1
        while x % i == 0:
            x = x / i
            b += 1
        n = b * n

    return n

a = 1
i = 2

while num_divisors(a) < 500:
    a += i
    i += 1

print a

