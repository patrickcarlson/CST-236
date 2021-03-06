#pylint: disable=too-few-public-methods
#Implemented by other
"""Module contains QA Class"""
class QA(object):
    """Class storing a question with its associated answer"""
    def __init__(self, question, answer):
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
