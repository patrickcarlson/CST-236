#pylint: disable=invalid-name, missing-docstring
# disabled due to names describing the function
"""
* Author:				Patrick Carlson
* Date Created:			02/27/2016
* Last Modification Date:	03/05/2016
* Assignment Number:    CST 236 Lab 6
* Filename:				performance_test.py
*
* Overview:
*	performance_test.py tests performance of question answer functionalities in
*   main. It tests requirements introduced that include a log file of questions
*   asked and the associated answers and that specific questions will process
*   in under a dictated time.
*
* Input:
*	Based on requirements provided.
*
* Output:
*	Will generate report in console concerning passing of tests, and html report concerning
*   coverage of code from the tests.
"""
from unittest import TestCase
import time
from source.main import Interface
from test.plugins.ReqTracer import requirements

def time_performance(question):
    qaobject = Interface()
    start_time = time.clock()
    qaobject.ask(question)
    total_time = time.clock() - start_time
    return total_time

class performancetests(TestCase):

    @requirements(['#0050', '#0051', '#0052'])
    def test_performance_logcheck(self):
        qaobject = Interface()
        start_time = time.clock()
        qaobject.ask("How many vowels are in : Apple?")
        total_time = time.clock() - start_time
        exists = False
        checkline = "How many vowels are in : Apple? : 2\n"
        with open('PerfLog.txt') as infile:
            for line in infile:
                if line == checkline:
                    exists = True
                    break
        self.assertTrue(exists)
        self.assertLess(total_time, .05)

    @requirements(['#0053'])
    def test_performance_rock_drop_question(self):
        total_time = time_performance("What is the velocity of a rock dropped from "
                                      "30 meters just before it hits the ground?")
        self.assertLess(total_time, .08)

    @requirements(['#0054'])
    def test_performance_triangle_type(self):
        total_time = time_performance("What type of triangle is 2.5 2.5 2.5")
        self.assertLess(total_time, .001)

    @requirements(['#0055'])
    def test_performance_boiling_temperature(self):
        total_time = time_performance("What is the boiling temperature, "
                                      "in degrees fahrenheit, at 15000 feet?")
        self.assertLess(total_time, .03)

    @requirements(['#0056'])
    def test_performance_change_return(self):
        total_time = time_performance("What is the smallest amount of coins that "
                                      "can be return for 5 dollars?")
        self.assertLess(total_time, .08)

    @requirements(['#0057'])
    def test_performance_vowel_count(self):
        total_time = time_performance("How many vowels are in Kalamazoo?")
        self.assertLess(total_time, .05)
