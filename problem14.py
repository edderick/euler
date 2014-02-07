def step(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

def check_chain(n):
    i = 1
    while True:
        x = step(n)
        if x == 1:
            break
        n = x
        i += 1

    return i + 1

best_score = 0
best_num = 0

for i in range(1, 1000000):
    x = check_chain(i)
    if x > best_score:
        best_score = x
        best_num = i

        print "n:{} len:{}".format(best_num, best_score)

