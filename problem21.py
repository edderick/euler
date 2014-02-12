# Intuition: Dynamic programming
# Reality, summing is pretty cheap, is this very self similar?

def d(n):
    proper_divisors = []
    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)

    return sum(proper_divisors)

amicable_numbers = set()

lim = 10000

for a in range(1, lim):
    b = d(a)
    if a == d(b) and a != b:
        if a < lim:
            amicable_numbers.add(a)
        if b < lim:
            amicable_numbers.add(b)

print amicable_numbers
print sum(amicable_numbers)
