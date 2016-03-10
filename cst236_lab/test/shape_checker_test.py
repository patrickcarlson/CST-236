#pylint: disable=invalid-name, missing-docstring
# disabled due to names describing the function
"""
* Author:				Patrick Carlson
* Date Created:			N/A
* Last Modification Date:	02/03/2016
* Assignment Number:    CST 236 Lab 2
* Filename:				shape_checker_test.py
*
* Overview:
*	Shape checker provides functions which will take sides, and angles, to output
*   whether the shape is a triangle(and what type of triangle it is), square, rectangle, or
*   rhombus. Shape checker test runs tests on the functions provided in shape checker.
*   Each test checks a different aspect of potential inputs that a user may expose the
*   shape checker to. Example code used as a template for this assignment provided by
*   instructor Josh Kimbal.
*
* Input:
*	Each of the shape checker functions are imported to the shape checker test. A seperate class is
*   set up for each of the shape checking functions.
*
* Output:
*	Outputs test results to console, and also outputs a list of requirements and which
*   test applies to each requirement in TraceOutput.txt.
*
"""
from unittest import TestCase
from source.shape_checker import get_triangle_type, get_squarerectangle_type, get_quadrilateral_type
from test.plugins.ReqTracer import requirements

class TestGetTriangleType(TestCase):
    """
    Tests for shape checker gettriangletype function
    """


    @requirements(['#0001', '#0002'])
    def test_get_triangle_fromtuple_all_int(self):
        a = (3, 2, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_fromdict_all_int(self):
        a = {'a': 1, 'b': 2, 'c': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_lessthanzero_all_int(self):
        result = get_triangle_type(-1, -1, -1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(3, 3, 2)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_nonintfloat_all_int(self):
        result = get_triangle_type('a', "DEADBEEF", 'Z')
        self.assertEqual(result, 'invalid')

class TestGetSquareRectangleType(TestCase):

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_lessthanzero_all_int(self):
        result = get_squarerectangle_type(-1, -1, -1, -1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_nonintfloat_all_char(self):
        result = get_squarerectangle_type('A', 'A', 'A', 'A')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_square_all_int(self):
        result = get_squarerectangle_type(2, 2, 2, 2,)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_square_all_float(self):
        result = get_squarerectangle_type(2.22, 2.22, 2.22, 2.22,)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_rectangle_all_int(self):
        result = get_squarerectangle_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_wronglength_all_int(self):
        result = get_squarerectangle_type(1, 2, 1, 3)
        self.assertEqual(result, 'invalid')

class TestGetQuadrilateralType(TestCase):

    @requirements(['#0004', '#0005'])
    def test_get_quadrilateral_side_non_int_float(self):
        result = get_quadrilateral_type('a', 'b', 'c', 'd', 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0004', '#0005'])
    def test_get_quadrilateral_angle_non_int_float(self):
        result = get_quadrilateral_type(14, 5, 14, 5, 'w', 'x', 'y', 'z')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_sidelessthanzero_all_int(self):
        result = get_quadrilateral_type(-1, -1, -1, -1, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadtrilateral_anglelessthanzero_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2, -5, -5, -5, -5)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_anglegreaterthanoneeighty_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 190, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_square_all_float(self):
        result = get_quadrilateral_type(2.4, 2.4, 2.4, 2.4, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_rectangle_all_int(self):
        result = get_quadrilateral_type(2, 4, 2, 4, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_rhombus_all_int(self):
        result = get_quadrilateral_type(3, 3, 3, 3, 44, 136, 44, 136)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_unequalsides_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 4, 50, 130, 50, 130)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_anglesnotequaltooneeighty_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4, 33, 146, 33, 146)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_angleboundariesunder_all_float(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 179.9, .1, 179.9, .1)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_angleboundariesequal_all_float(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 180.0, 0, 180.0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_angleboundariesover_all_float(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 180.1, .1, 180.1, .1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_parrallelogram(self):
        result = get_quadrilateral_type(4, 5, 4, 5, 110, 70, 110, 70)
        self.assertEqual(result, 'invalid')
