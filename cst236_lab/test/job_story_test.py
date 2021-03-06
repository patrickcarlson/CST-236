"""
* Author:				Patrick Carlson
* Date Created:			01/23/2016
* Last Modification Date:	02/03/2016
* Assignment Number:    CST 236 Lab 3
* Filename:				job_story_test.py
*
* Overview:
*	Tests provided job stories in ProjectRequirements.txt
*
* Input:
*	Takes in a string equal to equivalent string in ProjectRequirements.txt
*   Imports Interface object from main, which is the code to be tested.
* Output:
*	Output to console with number of tests, and whether succesful, also updates TraceOutput.txt
*   with which tests correspeond with which project requirements.
"""
import time
import getpass
from unittest import TestCase
from source.main import Interface
from test.plugins.ReqTracer import story

class JobStoryQuestions(TestCase):
    """
    Tests for provided job stories in ProjectRequirements.txt
    """

    @story(['When I ask "What time is it?" I want to be given the current '
            'date/time so I can stay up to date'])
    def test_question_current_time_date(self):
        """
        Tests "What time is it?" question.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What time is it?")
        currenttime = time.strftime('%c')
        self.assertEqual(result, currenttime)

    @story(['When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t'
            ' have to figure it out myself'])
    def test_question_fib_nth(self):
        """
        Tests fibonacci sequence function
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the 8 digit of fibonacci?")
        self.assertEqual(result, 21)

    @story(['When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t'
            ' have to figure it out myself'])
    def test_question_fib_nth_float(self):
        """
        Test invalid return for float entry, fibonacci.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the 8.55 digit of fibonacci?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t'
            ' have to figure it out myself'])
    def test_question_fib_negativeinput(self):
        """
        Tests for invalid return with negative entry of fibonacci.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the -8 digit of fibonacci?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have'
            ' to figure it out myself'])
    def test_question_pi_nthdigit_float(self):
        """
        Test for invalid return of float entry for Pi function.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the 3.5 digit of pi?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have'
            ' to figure it out myself'])
    def test_question_pi_nth_negative(self):
        """
        Tests for invalid return upon negative entry of Pi function
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the -22 digit of pi?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have'
            ' to figure it out myself'])
    def test_question_pi_nthdigit(self):
        """
        Tests for correct result of valid entries in Pi function.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the 3 digit of pi?")
        self.assertEqual(result, 4)
        result = qaobject.ask("What is the 9 digit of pi?")
        self.assertEqual(result, 5)
        # Need more decimal places
        # result = qaobject.ask("What is the 28 digit of pi?")
        # self.assertEqual(result, 2)

    @story(['When I ask "Please clear memory" I was the application to clear user set questions'
            ' and answers so I can reset the application'])
    def test_request_clearmemory(self):
        """
        Tests memory clearing request.
        :return:
        """
        qaobject = Interface()
        qaobject.ask("What color is the cow?")
        qaobject.teach("brown")
        result = qaobject.ask("What color is the cow?")
        self.assertEqual(result, 'brown')
        qaobject.request("Please clear memory")
        result = qaobject.teach('blue')
        self.assertEqual(result, "Please ask a question first")
        result = qaobject.ask("What color is the cow?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @story(['When I say "Open the door hal", I want the application to say "I\'m afraid I can\'t'
            ' do that <user name> so I know that is not an option'])
    def test_request_hal_open_door(self):
        """
        Tests correct returns of Hal request.
        :return:
        """
        qaobject = Interface()
        result = qaobject.request("Open the door hal")
        halandusername = "I'm afraid I can't do that " + getpass.getuser()
        self.assertEqual(result, halandusername)

    @story(['When I ask "Convert <number> <units> to <units>" I want to receive the converted value'
            ' and units so I can know the answer.'])
    def test_request_convert_single(self):
        """
        Check correct unit conversion.
        :return:
        """
        qaobject = Interface()
        result = qaobject.request("Convert 10 meters to kilometers")
        self.assertEqual(result, "0.01 kilometers")

    @story(['When I ask for a numberic conversion I want at least 10 different units I can convert'
            ' from/to'])
    def test_request_convert_tenunits(self):
        """
        Test all unit conversions.
        :return:
        """
        qaobject = Interface()
        result = qaobject.request("Convert 10 meters to kilometers")
        self.assertEqual(result, "0.01 kilometers")
        result = qaobject.request("Convert 10 meters to megameters")
        self.assertEqual(result, "0.00001 megameters")
        result = qaobject.request("Convert 10 meters to decameters")
        self.assertEqual(result, "1.0 decameters")
        result = qaobject.request("Convert 10 meters to hectometers")
        self.assertEqual(result, "0.1 hectometers")
        result = qaobject.request("Convert 10 meters to gigameters")
        self.assertEqual(result, "0.00000001 gigameters")
        result = qaobject.request("Convert 10 meters to terameters")
        self.assertEqual(result, "0.00000000001 terameters")
        result = qaobject.request("Convert 10 meters to decimeters")
        self.assertEqual(result, "100.0 decimeters")
        result = qaobject.request("Convert 10 meters to centimeters")
        self.assertEqual(result, "1000.0 centimeters")
        result = qaobject.request("Convert 10 meters to millimeters")
        self.assertEqual(result, "10000.0 millimeters")
        result = qaobject.request("Convert 10 meters to micrometers")
        self.assertEqual(result, "10000000.0 micrometers")



    @story(['When I ask for a numberic conversion I want at least 10 different units I can'
            ' convert from/to'])
    def test_request_convert_unknown(self):
        """
        Test invalid entry for units in conversion request.
        :return:
        """
        qaobject = Interface()
        result = qaobject.request("Convert 10 cups to gallons")
        self.assertEqual(result, "Unknown unit")

    @story(['When I ask "What color is the kitten?" I want to be given a random color.'])
    def test_ask_cat_color(self):
        """
        Test random result of colored kitten question.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What color is the kitten?")
        self.assertTrue(result in qaobject.colors)
        result = qaobject.ask("What color is the kitten?")
        self.assertTrue(result in qaobject.colors)

    @story(['When I ask "How many vowels are in: <word>?" I want a number telling me how many'
            ' vowels are in the word.'])
    def test_ask_vowels_word(self):
        """
        Check correct return on number of vowels in provided string.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("How many vowels are in : Apple?")
        self.assertEqual(result, 2)

    @story(['When I say "Go Owls!" I want to be return the string "Hoo Hoo"'])
    def test_request_hooting(self):
        """
        Check Go Owl's request returns correct string.
        :return:
        """
        qaobject = Interface()
        result = qaobject.request("Go Owls!")
        self.assertEqual(result, 'Hoo Hoo')

    @story(['Any time someone requests "Go Owls" the last question should be set to "What is'
            ' OIT?" and the answer should be "Oregon Institue of Technology'])
    def test_request_hoot_update(self):
        """
        Check that What is OIT question answer overwrites request response
        :return:
        """
        qaobject = Interface()
        qaobject.request("Go Owls!")
        result = qaobject.ask("What is OIT?")
        self.assertEqual(result, "Oregon Institute of Technology")

    @story(['Any time someone asks "What is the airspeed velocity of a laden swallow" the'
            ' application should ask whether european or african'])
    def test_monty_python_swallow(self):
        """
        Check that Swallow question return appropriate response for bridge crossing.
        :return:
        """
        qaobject = Interface()
        result = qaobject.ask("What is the airspeed velocity of a laden swallow?")
        self.assertEqual(result, "African or European?")
