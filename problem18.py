l = []

l.append([75])
l.append([95, 64])
l.append([17, 47, 82])
l.append([18, 35, 87, 10])
l.append([20,  4, 82, 47, 65])
l.append([19,  1, 23, 75,  3, 34])
l.append([88,  2, 77, 73,  7, 63, 67])
l.append([99, 65,  4, 28,  6, 16, 70, 92])
l.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
l.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
l.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
l.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
l.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
l.append([63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
l.append([ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23])

for last_row, row in zip(l, l[1:len(l)+1]):
    for i, v in enumerate(row):
        p = []
        
        if i > 0:
            p.append(last_row[i-1])
        if i < len(row) - 1:
            p.append(last_row[i])

        row[i] = max(p) + v

for row in l:
    print row

print "Max: {}".format(max(l[-1]))
