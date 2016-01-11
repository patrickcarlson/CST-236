"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
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

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return 'invalid'

    if not (isinstance(ab, (int, float)) and isinstance(bc, (int, float)) and isinstance(cd, (int, float)) and isinstance(da, (int, float))):
        return 'invalid'

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return 'invalid'

    if ab <= 0 or bc <= 0 or cd <= 0 or da <= 0:
        return 'invalid'

    if ab >= 180 or bc >= 180 or cd >= 180 or da >= 180:
        return 'invalid'

    if a == b and b == c and c == d and ab == 90 and bc == 90 and cd == 90 and da == 90:
        return 'square'

    if a == c and b == d and ab == 90 and bc == 90 and cd == 90 and da == 90:
        return 'rectangle'

    if a == b and b == c and c == d and ab == cd and bc == da and ab + bc == 180:
        return 'rhombus'

    else:
        return 'disconnected'