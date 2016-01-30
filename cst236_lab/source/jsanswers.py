from math import sqrt, pi
import time

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
    if n < 0:
        return 'invalid'
    if isinstance(n, (int, float)):
        int(n)
        digit = ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))
        return int(digit)

"""
#returns nth digit of pi. if n provided has decimal digits, returns invalid
"""
def get_nth_digit_pi(n = 0):
    if not isinstance( n, ( int, long ) ):
        return 'invalid'

