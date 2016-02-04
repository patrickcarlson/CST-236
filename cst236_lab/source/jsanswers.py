"""
* Author:				Patrick Carlson
* Date Created:			01/23/2016
* Last Modification Date:	02/03/2016
* Assignment Number:    CST 236 Lab 3
* Filename:				jsanswers.py
*
* Overview:
*	jsanswers.py contains additional functions for main.py to utilize in answering
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

from math import sqrt, pi
import time, random
from decimal import Decimal


"""
#returns current time and date based on local.
"""
def get_current_time_date():
    localtime = time.strftime('%c')
    return localtime

"""
#returns nth digit of fibonacci sequence. n is argument provided.
#Fibonacci equation is Fn = ((1 + 5^(1/2))^n - (1 - 5^(1/2))^n) / (2^n * 5^(1/2))
"""
def get_nth_digit_fibonacci(n=0):
    if n > 0 and float.is_integer(n):
        digit = ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))
        return int(digit)
    else:
        return 'invalid'


"""
#returns nth digit of pi. if n provided has decimal digits, returns invalid
"""
def get_nth_digit_pi(n = 0):

#todo(Patrick) Not getting enough digits out of pi, import a .txt with million?
    if n > 0 and float.is_integer(n):
        n = int(n)
        digit = (Decimal(pi) * 10**(n-1)) % 10
        digit = Decimal(digit) - Decimal(digit) % 1
        return digit
    else:
        return 'invalid'

def get_cat_color():
    colors = ['White', 'Brown', 'Blue', 'Green', 'Purple', 'Orange', 'Black']
    index = random.randint(0, 6)
    return colors[index]

def get_vowel_count(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vcount = 0
    for c in word:
        if c.lower() in vowels:
            vcount += 1
    return vcount