fn1 = 0
fn = 1

n = 1

while (len(str(fn)) < 1000):
    tmp = fn
    fn = fn1 + fn
    fn1 = tmp
    n += 1

print fn
print n
