"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type, get_squarerectangle_type, get_quadrilateral_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_fromtuple_all_int(self):
        a = (3, 2, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_fromdict_all_int(self):
        a = {'a': 1, 'b': 2, 'c': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_lessthanzero_all_int(self):
        result = get_triangle_type(-1, -1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(3, 3, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_nonintfloat_all_int(self):
        result = get_triangle_type('a', "DEADBEEF", 'Z')
        self.assertEqual(result, 'invalid')

class TestGetSquareRectangleType(TestCase) :

    def test_get_squarerectangle_lessthanzero_all_int(self):
        result = get_squarerectangle_type(-1, -1 , -1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_squarerectangle_nonintfloat_all_char(self):
        result = get_squarerectangle_type('A', 'A', 'A', 'A')
        self.assertEqual(result, 'invalid')

    def test_get_squarerectangle_square_all_int(self):
        result = get_squarerectangle_type(2, 2, 2, 2,)
        self.assertEqual(result, 'square')

    def test_get_squarerectangle_square_all_float(self):
        result = get_squarerectangle_type(2.22, 2.22, 2.22, 2.22,)
        self.assertEqual(result, 'square')

    def test_get_squarerectangle_rectangle_all_int(self):
        result = get_squarerectangle_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_squarerectangle_wronglength_all_int(self):
        result = get_squarerectangle_type(1, 2, 1, 3)
        self.assertEqual(result, 'invalid')

class TestGetQuadrilateralType(TestCase) :

    def test_get_quadrilateral_sidelessthanzero_all_int(self):
        result = get_quadrilateral_type(-1, -1, -1, -1, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadtrilateral_anglelessthanzero_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2, -5, -5, -5, -5)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_anglegreaterthanoneeighty_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 190, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_square_all_float(self):
        result = get_quadrilateral_type(2.4, 2.4, 2.4, 2.4, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rectangle_all_int(self):
        result = get_quadrilateral_type(2, 4, 2, 4, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_rhombus_all_int(self):
        result = get_quadrilateral_type(3, 3, 3, 3, 44, 136, 44, 136)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_unequalsides_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 4, 50, 130, 50, 130)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_anglesnotequaltooneeighty_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4, 33, 146, 33, 146)
        self.assertEqual(result, 'disconnected')