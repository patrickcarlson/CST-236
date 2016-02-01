import time, os, getpass
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
        #todo(Patrick) Need more decimal places
        # result = qaobject.ask("What is the 28 digit of pi?")
        # self.assertEqual(result, 2)

    @story(['When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application'])
    def test_request_clearmemory(self):
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

    @story(['When I say "Open the door hal", I want the application to say "I\'m afraid I can\'t do that <user name> so I know that is not an option'])
    def test_request_hal_open_door(self):
        qaobject = Interface()
        result = qaobject.request("Open the door hal")
        halandusername = "I'm afraid I can't do that " + getpass.getuser()
        self.assertEqual(result, halandusername)

#todo(Patrick) Implement unit coversion
    @story(['When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can know the answer.'])
    def test_request_covert_units_single(self):
        qaobject = Interface()
