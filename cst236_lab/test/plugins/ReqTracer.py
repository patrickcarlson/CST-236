"""
* Author:				Patrick Carlson
* Date Created:			N/A
* Last Modification Date:	01/23/2016
* Assignment Number:    CST 236 Lab 2
* Filename:				ReqTracer.py
*
* Overview:
*	ReqTracer provides the ability for a nose2 test to import a list of requirements and also
*   the ability to trace requirements to tests, which will output to TraceOutput.txt once tests have
*   run. All functionality provided by Josh Kimbal, RequirementTraceOutput(Plugin) class written
*   by Patrick Carlson
*
* Input:
*	Imports a txt of requirements, in TracerInputReqs.txt.
*
* Output:
*	RequirementTraceOutput class will write requirement traces to TraceOutput.txt.
*
"""

import logging
import os

from nose2.events import Plugin

class RequirementTraceOutput(Plugin):

    configSection = 'req-tracer'

    def afterSummaryReport(self, event):
        with open('TraceOutput.txt', 'w') as f:
            for key, item in sorted(Requirements.items()):
                f.write(key + ' ' + str(item.func_name) + '\n')
            for item in Stories:
                f.write(item.JStext + ' ' + str(item.func_name) + '\n')

class RequirementTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

class JSTrace(object):
    JStext = ""
    def __init__(self, text):
        self.JStext = text
        self.func_name = []

Requirements = {}

Stories = []

def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


def story(story_list):
    def wrapper(func):
        def add_story_and_call(*args, **kwargs):
            for st in story_list:
                for item in Stories:
                    if item.JStext.lower() == st.lower():
                        item.func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_story_and_call

    return wrapper

with open('ProjectRequirements.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)
        if '*' in line:
            storyadd = line.lstrip('* ')
            storyadd = storyadd.rstrip('\n')
            Stories.append(JSTrace(storyadd))