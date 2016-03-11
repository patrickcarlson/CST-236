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
    def test_get_triangle_tuple_all_int(self):
        """
        tests triangle type, assert scalene
        :return:
        """
        triangle = (3, 2, 1)
        result = get_triangle_type(triangle)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_dict_all_int(self):
        """
        Tests retrieving triangle from dict.
        :return:
        """
        triangle = {'a': 1, 'b': 2, 'c': 3}
        result = get_triangle_type(triangle)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equil_all_int(self):
        """
        Check correct return for equilateral triangle
        :return:
        """
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scal_all_int(self):
        """
        Check that for triangle scalene
        :return:
        """
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_ltz_all_int(self):
        """
        Test that invalid thrown when side value less than zero entered
        :return:
        """
        result = get_triangle_type(-1, -1, -1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_iso_all_int(self):
        """
        test for isosceles triangle
        :return:
        """
        result = get_triangle_type(3, 3, 2)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_input_all_int(self):
        """
        Test for invalid input
        :return:
        """
        result = get_triangle_type('a', "DEADBEEF", 'Z')
        self.assertEqual(result, 'invalid')

class TestGetSquareRectangleType(TestCase):
    """
    Tests for square and rectangle shape checker functions.
    """

    @requirements(['#0003', '#0004'])
    def test_get_squarerect_ltz_all_int(self):
        """
        Test square for less than zero inputs. invalid
        :return:
        """
        result = get_squarerectangle_type(-1, -1, -1, -1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_squarerectangle_char(self):
        """
        Test invalid input type of char. Invalid
        :return:
        """
        result = get_squarerectangle_type('A', 'A', 'A', 'A')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_squarerect_sqr_all_int(self):
        """
        Check for square return.
        :return:
        """
        result = get_squarerectangle_type(2, 2, 2, 2,)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_sqrrect_sqr_all_float(self):
        """
        Check for square return, with float sides.
        :return:
        """
        result = get_squarerectangle_type(2.22, 2.22, 2.22, 2.22,)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_sqrrect_rect_all_int(self):
        """
        Check for rectangle return. In sides.
        :return:
        """
        result = get_squarerectangle_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004'])
    def test_get_sqrrect_length_all_int(self):
        """
        Check for invalid return, uneven sides.
        :return:
        """
        result = get_squarerectangle_type(1, 2, 1, 3)
        self.assertEqual(result, 'invalid')

class TestGetQuadrilateralType(TestCase):
    """
    Testing get quadrialteral type functions.
    """

    @requirements(['#0004', '#0005'])
    def test_get_quad_side_char(self):
        """
        check for invalid return. Char inputs for sides.
        :return:
        """
        result = get_quadrilateral_type('a', 'b', 'c', 'd', 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0004', '#0005'])
    def test_get_quad_angle_char(self):
        """
        check for invalid return. Char inputs for angles.
        :return:
        """
        result = get_quadrilateral_type(14, 5, 14, 5, 'w', 'x', 'y', 'z')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_sideltz_all_int(self):
        """
        Check for invalid return. Sides less than zero.
        :return:
        """
        result = get_quadrilateral_type(-1, -1, -1, -1, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_angleltz_all_int(self):
        """
        Check for invalid return. Angles less than zero.
        :return:
        """
        result = get_quadrilateral_type(2, 2, 2, 2, -5, -5, -5, -5)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_gtr180_all_int(self):
        """
        Check for invalid return. Angle greater than 180 degrees.
        :return:
        """
        result = get_quadrilateral_type(2, 2, 2, 2, 190, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_all_float(self):
        """
        Check returns square with floats sides.
        :return:
        """
        result = get_quadrilateral_type(2.4, 2.4, 2.4, 2.4, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rect_all_int(self):
        """
        check for rectangle return. int sides.
        :return:
        """
        result = get_quadrilateral_type(2, 4, 2, 4, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_all_int(self):
        """
        Check for rhombus return, int sides.
        :return:
        """
        result = get_quadrilateral_type(3, 3, 3, 3, 44, 136, 44, 136)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_sidedisc_all_int(self):
        """
        Check for disconnected return, sides.
        :return:
        """
        result = get_quadrilateral_type(2, 2, 2, 4, 50, 130, 50, 130)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_anglover_all_int(self):
        """
        Check for disconnected return, angles.
        :return:
        """
        result = get_quadrilateral_type(1, 2, 3, 4, 33, 146, 33, 146)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_under_all_float(self):
        """
        Check for rhombus return. float angles.
        :return:
        """
        result = get_quadrilateral_type(2, 2, 2, 2, 179.9, .1, 179.9, .1)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_angl180_all_float(self):
        """
        Check for invalid, opposite angles 180 degrees.
        :return:
        """
        result = get_quadrilateral_type(2, 2, 2, 2, 180.0, 0, 180.0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_angover_all_float(self):
        """
        Check for invalid return. Angles over 360 degrees total. float
        :return:
        """
        result = get_quadrilateral_type(2, 2, 2, 2, 180.1, .1, 180.1, .1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_parrallelogram(self):
        """
        Check for invalid return. Non rhombus parrallelogram.
        :return:
        """
        result = get_quadrilateral_type(4, 5, 4, 5, 110, 70, 110, 70)
        self.assertEqual(result, 'invalid')
