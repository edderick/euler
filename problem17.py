
## There are more pythonic ways to do it, but this works..

def to_letters(n):
    s = str(n)

    if len(s) == 4:
        return "onethousand"
    elif len(s) == 3:
        if n % 100 == 0:
            return to_letters(int(s[0])) + "hundred"
        return to_letters(int(s[0])) + "hundredand" + to_letters(int(s[1]+s[2]))
    elif len(s) == 2:
        if s[0] == "9":
            return "ninety" + to_letters(s[1])
        if s[0] == "8":
            return "eighty" + to_letters(s[1])
        if s[0] == "7":
            return "seventy" + to_letters(s[1])
        if s[0] == "6":
            return "sixty" + to_letters(s[1])
        if s[0] == "5":
            return "fifty" + to_letters(s[1])
        if s[0] == "4":
            return "forty" + to_letters(s[1])
        if s[0] == "3":
            return "thirty" + to_letters(s[1])
        if s[0] == "2":
            return "twenty" + to_letters(s[1])
        if s[0] == "1":
            if s[1] == "9": 
                return "nineteen"
            if s[1] == "8":
                return "eighteen"
            if s[1] == "7": 
                return "seventeen"
            if s[1] == "6":
                return "sixteen"
            if s[1] == "5": 
                return "fifteen"
            if s[1] == "4":
                return "fourteen"
            if s[1] == "3":
                return "thirteen"
            if s[1] == "2":
                return "twelve"
            if s[1] == "1":
                return "eleven"
            if s[1] == "0":
                return "ten"
    elif len(s) == 1:
        if s[0] == "9": 
            return "nine"
        if s[0] == "8":
            return "eight"
        if s[0] == "7": 
            return "seven"
        if s[0] == "6":
            return "six"
        if s[0] == "5": 
            return "five"
        if s[0] == "4":
            return "four"
        if s[0] == "3":
            return "three"
        if s[0] == "2":
            return "two"
        if s[0] == "1":
            return "one"
        return ""

print sum([len(to_letters(i)) for i in range(1, 1001)])
