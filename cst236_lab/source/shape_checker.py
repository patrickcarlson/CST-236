
"""
* Author:				Patrick Carlson
* Date Created:			N/A
* Last Modification Date:	01/13/2016
* Assignment Number:    CST 236 Lab 1
* Filename:				shape_checker.py
*
* Overview:
*	Shape checker provides functions which will take sides, and angles, to output
*   whether the shape is a triangle(and what type of triangle it is), square, rectangle, or
*   rhombus. Example code used as a template for this assignment provided by instructor Josh
*   Kimbal
*
* Input:
*	Each function takes in values for the sides of the shape, single character variables represent
*   side values, and 2 character variables represent the angle between two sides.
*
* Output:
*	Each function returns a string representative of the findings from the inputted sides/angles.
"""


def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def get_squarerectangle_type(a=0, b=0, c=0, d=0):
    """

    Determine if the provided quadrilateral is a Square or Rectangle

    :param a: line a
    :type float or int

    :param b: line b
    :type float or int

    :param c: line c
    :type float or int

    :param d: line d
    :type float or int

    :return: str
    """

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"

    if a == c and b == d:
        return "rectangle"

    else:
        return "invalid"

def get_quadrilateral_type(a=0, b=0, c=0, d=0, ab=0, bc=0, cd=0, da=0):
    """

    Determine if the provided quadrilateral is a square, rectangle, or rhombus.
    :param a: line 1
    :type float or int

    :param b: line 2
    :type float or int

    :param c: line 3
    :type float or int

    :param d: line 4
    :type float or int

    :param ab: angle ab
    :type float or int

    :param bc: angle bc
    :type float or int

    :param cd: angle cd
    :type float or int

    :param da: angle da
    :type float or int

    :return: str
    """

    """
    " Check that inputted value is float or int. return invalid if not
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return 'invalid'

    """
    " Check that inputted value is float or int. return invalid if not
    """
    if not (isinstance(ab, (int, float)) and isinstance(bc, (int, float)) and isinstance(cd, (int, float)) and isinstance(da, (int, float))):
        return 'invalid'

    """
    " Check that inputted side values are greater than zero. return invalid if not
    """
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return 'invalid'
    """
    " Check that inputted angle values are greater than zero. return invalid if not
    """
    if ab <= 0 or bc <= 0 or cd <= 0 or da <= 0:
        return 'invalid'

    """
    " Check that inputted angle values are less than 180 degrees. return invalid if not
    """
    if ab >= 180 or bc >= 180 or cd >= 180 or da >= 180:
        return 'invalid'

    """
    " Check whether inputted values represent a parrallelogram instead of a rhombus. If
    " True, return invalid.
    """
    if ab != 90 and ab + bc == 180 and cd + da == 180 and a != b and a == c and b == d:
        return 'invalid'

    if a == b and b == c and c == d and ab == 90 and bc == 90 and cd == 90 and da == 90:
        return 'square'

    if a == c and b == d and ab == 90 and bc == 90 and cd == 90 and da == 90:
        return 'rectangle'

    if a == b and b == c and c == d and ab == cd and bc == da and ab + bc == 180:
        return 'rhombus'

    else:
        return 'disconnected'