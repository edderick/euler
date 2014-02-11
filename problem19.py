day = 1
month = 1
year = 1900

SUNDAY = 6
SEP, APR, JUN, NOV, FEB, DEC = 9, 4, 6, 11, 2, 12

day_of_week = 0

num_first_sundays = 0

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def fix_date(day, month, year):
    days_in_month = 31

    if month == FEB:
        if is_leap_year(year):
            days_in_month = 29
        else:
            days_in_month = 28
    elif month == SEP or month == APR or month == JUN or month == NOV:
        days_in_month = 30

    if day > days_in_month:
        month += 1
        day = 1

    if month > DEC:
        year += 1
        month = 1

    return day, month, year

while day != 31 or month != 12 or year != 2000:
    day_of_week = (day_of_week + 1) % 7
    day += 1

    day, month, year = fix_date(day, month, year)

    if day_of_week == SUNDAY and day == 1 and year > 1900:
        num_first_sundays += 1

print num_first_sundays
