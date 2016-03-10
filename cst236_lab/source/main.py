"""
* Author:				Patrick Carlson
* Date Created:			N/A
* Last Modification Date:	02/03/2016
* Assignment Number:    CST 236 Lab 3
* Filename:				main.py
*
* Overview:
*	main.py contains the Interface object, created by Josh Kimball, which is used as
*  a question and answer system. It supports a number of known questions and requests, but
*  can also be taught answers to questions. Example code used as a template for this
*  assignment provided by instructor Josh Kimbal
*
* Input:
*	Input is in the form of strings from console.
*
* Output:
*	Strings, chars, or ints/floats to console as answers to questions provided in string form.
"""
#pylint: disable=, missing-docstring
# Implemented by other
import difflib
import copy
import getpass
from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answerfuncs import get_current_time_date, get_nth_digit_pi, get_nth_digit_fibonacci, \
    get_cat_color, get_vowel_count, get_coin_return, get_triangle_angles, \
    get_velocity_dropped_item, get_boiling_elevation
from source.git_utils import  is_file_in_repo, get_git_file_info, get_file_info, get_repo_branch, \
    get_repo_url


NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):  #pylint: disable=too-many-instance-attributes
    def __init__(self):   #Implemented by other
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", 'Is']
        self.question_mark = chr(0x3F)

        self.units = {'micrometers' : -6, 'millimeters' : -3, 'centimeters' : -2,
                      'decimeters' : -1, 'meters' : 0, 'decameters' : 1, 'hectometers' : 2,
                      'kilometers': 3, 'megameters' : 6, 'gigameters' : 9, 'terameters' : 12}

        self.colors = ['White', 'Brown', 'Blue', 'Green', 'Purple', 'Orange', 'Black']

        self.question_answers_default = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ',
                                                 get_quadrilateral_type),
            'What time is it' :QA('What time is it', get_current_time_date),
            'What is the digit of fibonacci' :QA('What is the digit of fibonacci',
                                                 get_nth_digit_fibonacci),
            'What is the digit of pi' :QA('What is the digit of pi', get_nth_digit_pi),
            'What color is the kitten' :QA('What color is the kitten', get_cat_color),
            'How many vowels are in ' : QA('How many vowels are in', get_vowel_count),
            'What is the airspeed velocity of a laden swallow' :
                QA('What is the airspeed velocity of a laden swallow', 'African or European?'),
            'What is the smallest amount of coins that can be returned for' :
                QA('What is  the smallest amount of coins that can be returned for',
                   get_coin_return),
            'What are the angle measurements of a right triangle with side lengths' :
                QA('What are the angle measurements of a right triangle with side lengths',
                   get_triangle_angles),
#           'How many days until my birthday' : QA('How many days until my birthday', get_day_to_birthday), #pylint: disable=line-too-long, bad-continuation
                                                                                                            #Broken birthday function removed for continuity
            'What is the velocity of a rock dropped from meters just before it hits the ground' : QA('What is the velocity of a rock dropped from meters just before it hits the ground', get_velocity_dropped_item),
            'What is the boiling temperature, in degrees fahrenheit, at feet' : QA('What is the boiling temperature, in degrees fahrenheit, at feet', get_boiling_elevation),
            'Is the in the repo' : QA('Is the in the repo', is_file_in_repo),
            'What is the status of' : QA('What is the status of', get_git_file_info),
            'What is the deal with' : QA('What is the deal with', get_file_info),
            'What branch is' : QA('What branch is', get_repo_branch),
            'Where did come from' : QA('Where did come from', get_repo_url)
        }
        self.question_answers = copy.deepcopy(self.question_answers_default)

        self.last_question = None


    def request(self, request):
        if not isinstance(request, str):
            raise Exception('Not A String')

        if request.lower() == "please clear memory":
            self.question_answers = copy.deepcopy(self.question_answers_default)
            self.last_question = None
            return

        if request.lower() == "open the door hal":
            return "I'm afraid I can't do that " + getpass.getuser()

        if request.split(' ')[0] == 'Convert':
            numamount = float(request.split(' ')[1])
            fromunit = request.split(' ')[2].lower()
            tounit = request.split(' ')[4].lower()
            if fromunit and tounit in self.units.keys():
                exponent = self.units.get(fromunit) - self.units.get(tounit)
                returnvalue = numamount * 10**exponent
                returnvalue = str('{:.16f}'.format(returnvalue))
                while returnvalue[-1] == '0':
                    returnvalue = returnvalue[:-1]
                if returnvalue[-1] == '.':
                    returnvalue = returnvalue + '0'
                return returnvalue + ' ' + tounit
            else:
                return "Unknown unit"

        if request.lower() == "go owls!":
            self.last_question = "What is OIT"
            self.teach("Oregon Institute of Technology")
            return 'Hoo Hoo'


    def ask(self, question=""):    #pylint: disable=too-many-branches
                                   #Implemented by other
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')


        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN

        else:
            parsed_question = ""
            args = []
            if question.split(' ')[0] == 'Is' and question.split(' ')[-1] == 'repo?':
                i = 0
                for keyword in question[:-1].split(' '):
                    if i == 2:
                        args.append(str(keyword))
                        i += 1
                    else:
                        parsed_question += "{0} ".format(keyword)
                        i += 1

            elif '<' in question:
                parsed_question += "{0} ".format(question.split('<')[0])
                args.append(question.split('<')[1].split('>')[0])
                if question.split('<')[1].split('>')[1] != '?':
                    parsed_question += "{0} ".format(question.split('<')[1].split('>')[1])
                else:
                    parsed_question = parsed_question[:-1]
            elif question.split(' ')[0] == 'How' and question.split(' ')[2] == 'vowels':
                for keyword in question[:-1].split(' '):
                    if parsed_question.endswith(': '):
                        args.append(str(keyword))
                    else:
                        parsed_question += "{0} ".format(keyword)

            else:
                for keyword in question[:-1].split(' '):
                    try:
                        args.append(float(keyword))
                    except:     #pylint: disable=bare-except
                                #Implemented by other
                        parsed_question += "{0} ".format(keyword)

            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            returnanswer = answer.function(*args)
                            logfile = open('PerfLog.txt', 'a')
                            logfile.write(question + " : " + str(returnanswer) + "\n")
                            return returnanswer
                        except:
                            raise Exception("Too many extra parameters")
            else: #pylint: disable=useless-else-on-loop
                  #Implemented by other
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)
