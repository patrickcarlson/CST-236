"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_fromtuple_all_int(self):
        a = (3, 2, 1)
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