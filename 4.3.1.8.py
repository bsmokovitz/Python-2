def is_year_leap(year):
    #
# Your code from LAB 4.3.1.6.
#
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
#
# Write your new code here.
#
    if is_year_leap(year) == True:
        if month == 2:
            return 29
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        else:
            return 30
    else:
        if month == 2:
            return 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        else:
            return 30


def day_of_year(year, month, day):
#
# Write your new code here.
#
    if is_year_leap(year) == True:
        if month == 1:
            return day
        elif month == 2:
            return 31 + day
        elif month == 3:
            return 60 + day
        elif month == 4:
            return 91 + day
        elif month == 5:
            return 121 + day
        elif month == 6:
            return 152 + day
        elif month == 7:
            return 182 + day
        elif month == 8:
            return 213 + day
        elif month == 9:
            return 244 + day
        elif month == 10:
            return 274 + day
        elif month == 11:
            return 305 + day
        elif month == 12:
            return 335 + day
    else:
        if month == 1:
            return day
        elif month == 2:
            return 31 + day
        elif month == 3:
            return 59 + day
        elif month == 4:
            return 90 + day
        elif month == 5:
            return 120 + day
        elif month == 6:
            return 151 + day
        elif month == 7:
            return 181 + day
        elif month == 8:
            return 212 + day
        elif month == 9:
            return 243 + day
        elif month == 10:
            return 273 + day
        elif month == 11:
            return 304 + day
        elif month == 12:
            return 334 + day

print(day_of_year(2000, 12, 31))

