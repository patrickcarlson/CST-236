"""
* Author:				Patrick Carlson
* Date Created:			01/23/2016
* Last Modification Date:	02/06/2016
* Assignment Number:    CST 236 Lab 4
* Filename:				answerfuncs.py
*
* Overview:
*	answerfuncs.py contains additional functions for main.py to utilize in answering
*   questions provided. js(Job Stories) is focused on providing functions to utilize
*   for the additional parameters provided by the added job stories in
*   ProjectRequirements.txt.
*
* Input:
*	Arguments are passed into these functions, generally, after being parsed out of
*   the provided question strings.
*
* Output:
*	Each function outputs an expected value in concurrence with the question it is
*   associated with.
"""

from math import sqrt, pi, floor, atan, log
import time
import random
from decimal import Decimal


def get_current_time_date():
    """Returns current date and time"""
    localtime = time.strftime('%c')
    return localtime


def get_nth_digit_fibonacci(digit=0):
    """
    #returns nth digit of fibonacci sequence. n is argument provided.
    #Fibonacci equation is Fn = ((1 + 5^(1/2))^n - (1 - 5^(1/2))^n) / (2^n * 5^(1/2))
    """
    if digit > 0 and float.is_integer(digit):
        digit = ((1 + sqrt(5)) ** digit - (1 - sqrt(5)) ** digit) / (2 ** digit * sqrt(5))
        return int(digit)
    else:
        return 'invalid'



def get_nth_digit_pi(digit=0):
    """
    #returns nth digit of pi. if n provided has decimal digits, returns invalid
    """

#todo(Patrick) Not getting enough digits out of pi, import a .txt with million?
    if digit > 0 and float.is_integer(digit):
        digit = int(digit)
        digit = (Decimal(pi) * 10 ** (digit - 1)) % 10
        digit = Decimal(digit) - Decimal(digit) % 1
        return digit
    else:
        return 'invalid'

def get_cat_color():
    """
    #returns random color of a cat.
    """
    colors = ['White', 'Brown', 'Blue', 'Green', 'Purple', 'Orange', 'Black']
    index = random.randint(0, 6)
    return colors[index]

def get_vowel_count(word):
    """
    #Returns total number of vowels in a string.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    vcount = 0
    for count in word:
        if count.lower() in vowels:
            vcount += 1
    return vcount


def get_coin_return(total):
    """
    #returns smallest amount of coins for change.
    """
    total *= 100
    amount = [25, 10, 5, 1]
    coins = [0, 0, 0, 0]
    i = 0
    for divisor in amount:
        coins[i] = floor(total / divisor)
        total -= coins[i] * divisor
        i += 1

    finaltally = str(int(coins[0])) + ' quarters, ' + str(int(coins[1])) + ' dimes, '\
                 + str(int(coins[2])) + ' nickels, and ' + str(int(coins[3])) + ' pennies.'

    return finaltally


def get_triangle_angles(sidea, sideb, sidec):
    """
    #returns angles of a right triangle. side1 is treated as adjacent and side2 is
    #treated as opposite of angle.
    """
    sides = [sidea, sideb, sidec]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    side1 = min(sides)
    sides.remove(side1)
    side2 = sides[0]
    if abs(hypotenuse ** 2 - (side1 ** 2 + side2 ** 2)) > 1.50:
        return 'Not a right triangle'
    angle = atan(side2/side1)
    angle = angle * 180/pi

    return "90.0 degrees, " + str(round(angle, 2)) + " degrees, and " +\
           str(round(90 - angle, 2)) + " degrees"

# """
# #returns the number of days until the birthday indicated
# """
# def get_day_to_birthday(month, day):
#     months = {1 : 0, 2 : 31, 3 : 59, 4 : 90, 5 : 120, 6 : 151,
#               7 : 181, 8 : 212, 9 : 243, 10 : 273, 11 : 304, 12 : 334}
#     bdaycount = months[month] + day
#     totaldays = 0
#     leapyear = (datetime.date.today().year - 2016) % 4 == 0
#     today = datetime.date.today().timetuple().tm_yday
#     if today > bdaycount:
#         totaldays = 365 - today + bdaycount
#     else:
#         totaldays = bdaycount - today
#
#     if leapyear and today < 60 and (bdaycount > 60 or bdaycount < today):
#         totaldays += 1
#
#     return totaldays


def get_velocity_dropped_item(height):
    """
    #returns velocity of an object released from a specific height, after falling a set distance
    """
    velocity = sqrt(2*9.8*height)
    return velocity


def get_boiling_elevation(altitude):
    """
    #returns the temperature at which water will boil at a given eleveation(feet)
    """
    pressure = 29.921 * (1 - .0000068753 * altitude)**5.2559
    boilingelevation = 49.161 * log(pressure) + 44.932

    return round(boilingelevation, 2)
    #Pressure (in. Hg) = 29.921* (1-6.8753*0.000001 * altitude, ft.)^5.2559
    #Boiling point = 49.161 * Ln (in. Hg) + 44.932







