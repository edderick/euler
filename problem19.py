day = 1
month = 1
year = 1900

SUNDAY = 6

day_of_week = 0

num = 0

while day != 31 or month != 12 or year != 2000:
    day_of_week = (day_of_week + 1) % 7

    if month == 2:
        if day < 28:
            day += 1
        elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 29:
                day += 1
            else:
                day = 1
                month += 1
        else:
            day = 1
            month += 1

    elif month == 9 or month == 4 or month == 6 or month == 11:
        if day < 30:
            day += 1
        else:
            day = 1
            month += 1

    elif month == 12:
        if day < 31:
            day += 1
        else:
            day = 1
            month = 1
            year += 1
    else:
        if day < 31:
            day += 1
        else:
            day = 1
            month += 1


    print day_of_week, day, month, year
    if day_of_week == SUNDAY and day == 1 and year > 1900:
        num += 1

print num
