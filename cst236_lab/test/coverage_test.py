"""
* Author:				Patrick Carlson
* Date Created:			02/02/2016
* Last Modification Date:	02/06/2016
* Assignment Number:    CST 236 Lab 4
* Filename:				coverage_test.py
*
* Overview:
*	coverage_test.py contains nose2 plugin test functions utilized to test the return
*   values of code provided in source/main and source/answerfuncs. Also utilizing a
*   coverage plugin which outputs an html file with information on code coverage from
*   these tests
*
* Input:
*	Utilizing job stories as input, for trace output.
*
* Output:
*	Will generate report in console concerning passing of tests, and html report concerning
*   coverage of code from the tests.
"""
from unittest import TestCase
from source.main import Interface
from test.plugins.ReqTracer import story

class CoverageJobStories(TestCase):
    """
    Class contains methods to test aspects of code that have not be tested yet, to provide for more
    coverage.
    """


    @story(['Any time someone asks "What is the smallest amount of coins that can be returned for :'
            ' <cash>?" the application should read back " x quarters, x dimes,'
            ' x nickels, and x pennies."'])
    def test_coin_count(self):
        """
        Checks coin count, with different configurations, for code coverage.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the smallest amount of coins that"
                              " can be returned for: 1.75?")
        self.assertEqual(result, "7 quarters, 0 dimes, 0 nickels, and 0 pennies.")
        result = qaobject.ask("What is the smallest amount of coins that"
                              " can be returned for: 1.23?")
        self.assertEqual(result, "4 quarters, 2 dimes, 0 nickels, and 3 pennies.")

    @story(['Any time someone asks "What are the angle measurements of a right triangle with'
            ' side lengths: 3 4 5?" the applications should return " <angle> degrees,'
            ' <angle> degrees, and <angle> degrees"'])
    def test_right_triangle_angles(self):
        """
        Does right angle triangle tests for code coverage.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What are the angle measurements of a right triangle"
                              " with side lengths: 3 4 5?")
        self.assertEqual(result, "90.0 degrees, 53.13 degrees, and 36.87 degrees")
        result = qaobject.ask("What are the angle measurements of a right triangle"
                              " with side lengths: 10 10 14.1?")
        self.assertEqual(result, "90.0 degrees, 45.0 degrees, and 45.0 degrees")
        result = qaobject.ask("What are the angle measurements of a right triangle"
                              " with side lengths: 6 6 6?")
        self.assertEqual(result, "Not a right triangle")

    # @story(['Any time someone asks "How many days until my birthday: <month> <day>?"'
    #         ' the application should return an integer number'])
    # def test_get_daysuntilbirthday(self):
    #     qaobject = Interface()
    #     result = qaobject.ask("How many days until my birthday: 9 13?")
    #     count = 257 - (datetime.date.today().timetuple().tm_yday)
    #     self.assertEqual(result, count)
    #     result = qaobject.ask("How many days until my birthday: 2 14?")
    #     count = 45 - (datetime.date.today().timetuple().tm_yday)
    #     self.assertEqual(result, count)
    #     result = qaobject.ask("How many days until my birthday: 1 15?")
    #     count = 365 - (datetime.date.today().timetuple().tm_yday) + 15 + 1
    #     self.assertEqual(result, count)


    @story(['Any time someone asks "What is the velocity of a rock dropped from <height>'
            ' meters just before it hits the ground?" the application will return the'
            ' velocity of the rock.'])
    def test_get_rock_dropped(self):
        """
        Checks rock drop question for code coverage.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the velocity of a rock dropped from 10 meters"
                              " just before it hits the ground?")
        self.assertEqual(result, 14)

    @story(['Any time someone asks "What is the boiling temperature, in degrees fahrenheit,'
            ' at <elevation> feet?" the application should return the temperature, in degrees'
            ' at which water will boil'])
    def test_get_boiing_elevation(self):
        """
        Checks boilng/elevation question for code coverage purposes.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the boiling temperaturem in degrees fahrenheit,"
                              " at 10000 feet?")
        self.assertEqual(result, 193.6)
