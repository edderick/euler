# Intuition: Dynamic programming
# Reality, summing is pretty cheap, is this very self similar?
import math

def d(n):
    proper_divisors = []
    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)

    return sum(proper_divisors)

amicable_numbers = []

lim = 10000

for a in range(1, lim):
    b = d(a)
    if b > a and a == d(b):
        amicable_numbers += [a, b]

print amicable_numbers
print sum(amicable_numbers)
