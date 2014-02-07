import math
in_num = 600851475143

max_lim = int(math.ceil(in_num / 2))

candidates = [i for i in range(2, max_lim) if in_num % i == 0]

def check_prime(c):
    for i in range(2, int(math.ceil(math.sqrt(c)))):
        if c % i == 0:
            return False
    return True

for c in reversed(candidates):
    if check_prime(c):
        print c
        exit()


print candidates
