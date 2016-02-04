"""
* Author:				Patrick Carlson
* Date Created:			01/16/2016
* Last Modification Date:	02/03/2016
* Assignment Number:    CST 236 Lab 2
* Filename:				QA_test.py
*
* Overview:
*	QA_test contains source code ustilized by the nose2 plugin to test
*   the main and question_answer code stored in source. A plugin has been added
*   to Nose2 to provide the ability for nose2 to read requirments from a txt file
*   and output what tests apply to the different criteria in a txt file called
*   TraceOutput.txt.
*
* Input:
*	Imports an Interface object from main.py in source. The interface object allows
*   for questions to be asked, with standard responses, and the ability to teach
*   answers for unknown questions.
*
* Output:
*	Writes to TraceOutput.txt with a list of the requirements and what tests apply
*   to each requirement.
*
"""
from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements

class testQuestionAnswer(TestCase):

    @requirements(['#0006', '#0007'])
    def test_question_string_attemptanswer(self):
        qaobject = Interface()
        result = qaobject.ask('What type of triangle is: 3 4 5?')
        self.assertEqual(result, 'scalene')

    @requirements(['#0006', '#0008'])
    def test_question_string_nokeyword(self):
        qaobject = Interface()
        result = qaobject.ask("Is that a dog?")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0009'])
    def test_question_string_noquestionmark(self):
        qaobject = Interface()
        result = qaobject.ask("What type of triangle is: 3 3 3")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0010'])
    def test_question_string(self):
        qaobject = Interface()
        result = qaobject.ask("What_type_of_triangle_is: 3 3 3?")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0005', '#0006', '#0007', '#0011'])
    def test_question_90percentkeywordmatch(self):
        qaobject = Interface()
        result = qaobject.ask("What type of quadrilteral is: 2 2 2 2 90 90 90 90?")
        self.assertEqual(result, 'square')

    @requirements(['#0006', '#0008', '#0011', '#0012'])
    def test_question_excludenumbers_matchcode(self):
        qaobject = Interface()
        result = qaobject.ask("What type 2 of trangle is: 2 2?")
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0013', '#0014'])
    def test_question_validmatch_returnanswer(self):
        qaobject = Interface()
        result = qaobject.ask("What of trangle is: 2 2 2?")
        self.assertEqual(result, 'I don\'t know, please provide the answer')
        result = qaobject.ask("What type of triangle is: 2.5 2.5 2.5?")
        self.assertEqual(result, 'equilateral')

    @requirements(['#0015', '#0016'])
    def test_question_answer_provideanswer(self):
        qaobject = Interface()
        result = qaobject.ask("What triangle is: 5, 6, 5?")
        self.assertEqual(result, 'I don\'t know, please provide the answer')
        qaobject.teach("isosceles")
        result = qaobject.ask("What triangle is: 5, 6, 5?")
        self.assertEqual(result, 'isosceles')

    @requirements(['#0017'])
    def test_question_answer_nopreviousquestion(self):
        qaobject = Interface()
        result = qaobject.teach("How now brown cow.")
        self.assertEqual(result, 'Please ask a question first')

    @requirements(['#0018'])
    def test_question_hasanswerfromprevious(self):
        qaobject = Interface()
        qaobject.ask("What triangle is: 5, 6, 5?")
        qaobject.teach("isosceles")
        result = qaobject.ask("What triangle is: 5, 6, 5?")
        self.assertEqual(result, 'isosceles')
        result = qaobject.teach("Two sides equal")
        self.assertEqual(result, 'I don\'t know about that. I was taught differently')

    @requirements(['#0019'])
    def test_question_updateanswer(self):
        qaobject = Interface()
        qaobject.ask("What triangle is: 5, 6, 5?")
        qaobject.teach("scalene")
        result = qaobject.ask("What triangle is: 5, 6, 5?")
        self.assertEqual(result, 'scalene')
        qaobject.correct('isosceles')
        result = qaobject.ask("What triangle is: 5, 6, 5?")
        self.assertEqual(result, 'isosceles')

    @requirements(['#0020'])
    def test_question_updateanswer_storepreviousquestion(self):
        qaobject = Interface()
        result = qaobject.ask("What color is the cow?")
        self.assertEqual(result, 'I don\'t know, please provide the answer')
        result = qaobject.teach("The cow is brown")
        self.assertEqual(result, None)
        result = qaobject.correct("The cow is red")
        self.assertEqual(result, None)
        result = qaobject.ask("What color is the cow?")
        self.assertEqual(result, 'The cow is red')

    @requirements(['#0021'])
    def test_question_updateanswer_nopreviousquestion(self):
        qaobject = Interface()
        result = qaobject.correct("42")
        self.assertEqual(result, 'Please ask a question first')

    @requirements(['#0022'])
    def test_request_notastring(self):
        qaobject = Interface()
        self.assertRaises(Exception, qaobject.request, 2555)

    @requirements(['#0022'])
    def test_ask_notastring(self):
        qaobject = Interface()
        self.assertRaises(Exception, qaobject.ask, 45566)

    @requirements(['#0023'])
    def test_ask_toomanyparamters(self):
        qaobject = Interface()
        self.assertRaises(Exception, qaobject.ask, "What type of triangle is: 3 4 5 6?")

