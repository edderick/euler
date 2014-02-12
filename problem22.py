def name_score(name):
    score = 0
    for char in name:
        score += (ord(char) - ord('A') + 1)
    return score

total = 0

with open('names.txt') as names_file:
    names = []

    for line in names_file:
        names += line.split(',')

    names = [x.strip('"') for x in names]

    names.sort()

    for i, name in enumerate(names):
        total += name_score(name) * (i + 1)

print total
