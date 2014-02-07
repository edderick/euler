def num_digits(x):
    num = 0
    while x > 0:
        x = x / 10
        num += 1

    return num

def get_digit(x, num):
    for i in range(1, num):
        x = x / 10
    return x % 10

def is_palendrome(x):
    hi = num_digits(x)
    lo = 1

    while hi >= lo:
        if(get_digit(x, hi) != get_digit(x, lo)):
            return False
        hi -= 1
        lo += 1

    return True

digits = 3

res = []

for i in reversed(range(10 ** (digits - 1), 10 ** digits)):
    for j in reversed(range(10 ** (digits -1), 10 ** digits)):
        if is_palendrome(i*j):
            res.append(i*j)

print sorted(res)[-1]
