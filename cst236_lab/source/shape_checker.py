
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


def get_triangle_type(sidea=0, sideb=0, sidec=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param sidea: line a
    :type sidea: float or int or tuple or list or dict

    :param sideb: line b
    :type sideb: float

    :param sidec: line c
    :type sidec: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(sidea, (tuple, list)) and len(sidea) == 3:
        sidec = sidea[2]
        sideb = sidea[1]
        sidea = sidea[0]

    if isinstance(sidea, dict) and len(sidea.keys()) == 3:     #pylint: disable=maybe-no-member
        values = []
        for value in sidea.values():     #pylint: disable=maybe-no-member
            values.append(value)
        sidea = values[0]
        sideb = values[1]
        sidec = values[2]

    if not (isinstance(sidea, (int, float)) and
            isinstance(sideb, (int, float)) and isinstance(sidec, (int, float))):

        return "invalid"

    if sidea <= 0 or sideb <= 0 or sidec <= 0:
        return "invalid"

    if sidea == sideb and sideb == sidec:
        return "equilateral"

    elif sidea == sideb or sidea == sidec or sideb == sidec:
        return "isosceles"
    else:
        return "scalene"

def get_squarerectangle_type(sidea=0, sideb=0, sidec=0, sided=0):
    """

    Determine if the provided quadrilateral is a Square or Rectangle

    :param sidea: line a
    :type float or int

    :param sideb: line b
    :type float or int

    :param sidec: line c
    :type float or int

    :param sided: line d
    :type float or int

    :return: str
    """

    if not (isinstance(sidea, (int, float)) and isinstance(sideb, (int, float)) and
            isinstance(sidec, (int, float)) and isinstance(sided, (int, float))):

        return "invalid"

    if sidea <= 0 or sideb <= 0 or sidec <= 0 or sided <= 0:
        return "invalid"

    if sidea == sideb and sideb == sidec and sidec == sided:
        return "square"

    if sidea == sidec and sideb == sided:
        return "rectangle"

    else:
        return "invalid"

def get_quadrilateral_type(sidea=0, sideb=0, sidec=0, sided=0,  #pylint: disable=too-many-arguments, too-many-return-statements
                           angleab=0, anglebc=0, anglecd=0, angleda=0):  #required for operation

    """

    Determine if the provided quadrilateral is a square, rectangle, or rhombus.
    :param sidea: line 1
    :type float or int

    :param sideb: line 2
    :type float or int

    :param sidec: line 3
    :type float or int

    :param sided: line 4
    :type float or int

    :param angleab: angle ab
    :type float or int

    :param anglebc: angle bc
    :type float or int

    :param anglecd: angle cd
    :type float or int

    :param angleda: angle da
    :type float or int

    :return: str
    """
    if not (isinstance(sidea, (int, float)) and isinstance(sideb, (int, float)) and
            isinstance(sidec, (int, float)) and isinstance(sided, (int, float))):

        return 'invalid'

    if not (isinstance(angleab, (int, float)) and isinstance(anglebc, (int, float)) and
            isinstance(anglecd, (int, float)) and isinstance(angleda, (int, float))):

        return 'invalid'


    if sidea <= 0 or sideb <= 0 or sidec <= 0 or sided <= 0:
        return 'invalid'

    if angleab <= 0 or anglebc <= 0 or anglecd <= 0 or angleda <= 0:
        return 'invalid'


    if angleab >= 180 or anglebc >= 180 or anglecd >= 180 or angleda >= 180:
        return 'invalid'


    if (angleab != 90 and angleab + anglebc == 180 and anglecd + angleda == 180 and #pylint: disable=too-many-boolean-expressions
            sidea != sideb and sidea == sidec and sideb == sided):
        return 'invalid'

    if (sidea == sideb and sideb == sidec and sidec == sided and angleab == 90 and #pylint: disable=too-many-boolean-expressions
            anglebc == 90 and anglecd == 90 and angleda == 90):
        return 'square'

    if (sidea == sidec and sideb == sided and angleab == 90 and #pylint: disable=too-many-boolean-expressions
            anglebc == 90 and anglecd == 90 and angleda == 90):
        return 'rectangle'

    if (sidea == sideb and sideb == sidec and sidec == sided and #pylint: disable=too-many-boolean-expressions
            angleab == anglecd and anglebc == angleda and angleab + anglebc == 180):
        return 'rhombus'

    else:
        return 'disconnected'
