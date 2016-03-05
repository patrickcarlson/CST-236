from source.main import Interface
from unittest import TestCase
import time
from test.plugins.ReqTracer import requirements
#
# class performancetests(TestCase):

    # @requirements(['#0050', '#0051', '#0052'])
    # def test_performance_logcheck(self):
    #     qaobject = Interface()
    #     start_time = time.clock()
    #     qaobject.ask("How many vowels are in : Apple?")
    #     total_time = time.clock() - start_time
    #     exists = False
    #     checkline = "How many vowels are in : Apple? : 2\n"
    #     with open('PerfLog.txt') as f:
    #         for line in f:
    #             if line == checkline:
    #                 exists = True
    #     self.assertTrue(exists)
    #     self.assertLess(total_time, .05)

