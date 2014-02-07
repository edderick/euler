top = 2000000

l = [True for i in range(0, top)]

l[0] = False
l[1] = False

import math
end = int(math.sqrt(top))

for i in range(2, end + 1):
    if l[i]:
        for j in range(2, int(top / i) + 1):
            if j * i >= top:
                continue
            l[j * i] = False

s = 0

for i, x in enumerate(l):
    if x:
        s += i

print s
