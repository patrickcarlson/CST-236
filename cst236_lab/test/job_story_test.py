import time
from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements, story

class jobstoryquestions(TestCase):

    @story(['When I ask "What time is it?" I want to be given the current date/time so I can stay up to date'])
    def test_question_current_time_date(self):
        qaobject = Interface()
        result = qaobject.ask("What time is it?")
        currenttime = time.strftime('%c')
        self.assertEqual(result, currenttime)

    @story(['When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself'])
    def test_question_fibonacci_nthdigit(self):
        qaobject = Interface()
        result = qaobject.ask("What is the 8 digit of fibonacci?")
        self.assertEqual(result, 21)

    @story(['When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself'])
    def test_question_fibonacci_nthdigit_float(self):
        qaobject = Interface()
        result = qaobject.ask("What is the 8.55 digit of fibonacci?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself'])
    def test_question_fibonacci_negativeinput(self):
        qaobject = Interface()
        result = qaobject.ask("What is the -8 digit of fibonacci?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself'])
    def test_question_pi_nthdigit_float(self):
        qaobject = Interface()
        result = qaobject.ask("What is the 3.5 digit of pi?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself'])
    def test_question_pi_nthdigit_negative(self):
        qaobject = Interface()
        result = qaobject.ask("What is the -22 digit of pi?")
        self.assertEqual(result, 'invalid')

    @story(['When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself'])
    def test_question_pi_nthdigit(self):
        qaobject = Interface()
        result = qaobject.ask("What is the 3 digit of pi?")
        self.assertEqual(result, 4)
        result = qaobject.ask("What is the 9 digit of pi?")
        self.assertEqual(result, 5)
        result = qaobject.ask("What is the 30 digit of pi?")
        self.assertEqual(result, 7)