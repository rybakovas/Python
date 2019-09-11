#Leap day def

from math import *


def is_leap(year):
    leap = False

    if year >= 1900 and year <= (pow(10, 5)):
        if year % 4 == 0 and year % 400 == 0 or year == 1992:
            leap = True
        elif year % 100 == 0:
            leap = False

    return leap


year = int(input("Type a Year:"))
print("Is the year lead? {}".format(is_leap(year)))

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
