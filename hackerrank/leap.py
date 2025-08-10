# Question:
# A leap year is a year with an extra day (February 29) added every 4 years to keep the calendar correct.
# Rules to check a leap year:
# 1. If the year is divisible by 400, it is a leap year.
# 2. Else if the year is divisible by 100, it is NOT a leap year.
# 3. Else if the year is divisible by 4, it is a leap year.
# 4. Otherwise, it is NOT a leap year.
#
# Task:
# Write a function is_leap(year) that returns True if the year is a leap year, else False.
#
# Input:
# An integer year to test.
#
# Output:
# Boolean True or False indicating if the year is leap year.

def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap=False    

    return leap

# Read input year from user
year = int(input())
print(is_leap(year))
