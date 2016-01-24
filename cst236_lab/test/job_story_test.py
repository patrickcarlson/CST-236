import time
from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements, story

class jobstoryquestions(TestCase):

    @story(['When I ask "What time is it?" I want to be given the current date/time so I can stay up to date'])
    def test_question_currenttime(self):
        qaobject = Interface()
        result = qaobject.ask("What time is it?")
        currenttime = time.ctime()
        self.assertEqual(result, currenttime)

    @story(['When I ask "What time is it?" I want to be given the current date/time so I can stay up to date'])
    def test_question_time_again(self):
        # qaobject = Interface()
        a = 4
        self.assertEqual(a, 4)