#pylint: disable=anomalous-unicode-escape-in-string, anomalous-backslash-in-string
#  anomalous portions part of input string
"""
* Author:				Patrick Carlson
* Date Created:			02/13/2016
* Last Modification Date:	02/24/2016
* Assignment Number:    CST 236 Lab 5
* Filename:				git_utils_test.py
*
* Overview:
*	git_utils_test.py runs test code on git_utils.py. The tests work by mocking
*   specific portions of git_utils, specifically the subprocess method, in
*   order to run these tests.
*
* Input:
*	Based on requirements provided for testing git_utils.py
*
* Output:
*	Will generate report in console concerning passing of tests, and html report concerning
*   coverage of code from the tests.
"""

from unittest import TestCase
from mock import mock, patch
from source.main import Interface
from source import git_utils
from test.plugins.ReqTracer import requirements

PARENT_DIRECTORY = __file__[:-23]

class GitUtilsTests(TestCase):
    """
    Contains functions for testing git_utils.py contained in source folder.
    Utilizes Mock.
    """

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_path_abs_bool(self, mock_subproc_popen):
        """
        Tests for file that exists in repo
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the nose2.cfg in the repo?")
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_path_exists_bool(self, mock_subproc_popen):
        """
        Checks path exists in repo
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the ProjectRequirements.txt in the repo?")
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_path_dne_bool(self, mock_subproc_popen):
        """
        Check for path which doesn't exist.
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the E:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab"
                              " in the repo?")
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_path_diff_bool(self, mock_subproc_popen):
        """
        Checks for existing file, that isn't in repo
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock = mock.Mock()
        attrs = {'communicate.return_value'
                 : ('didntcommit.txt', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the <didntcommit.txt> in the repo?")
        self.assertEqual(result, 'No')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_localmod(self, mock_subproc_popen):
        """
        Checks for return of file that has only been modified locally
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value': ("didntcommit.txt", '')}
        p_mock1.configure_mock(**attrs)
        p_mock2 = mock.Mock()
        attrs = {'communicate.return_value': (PARENT_DIRECTORY, '')}
        p_mock2.configure_mock(**attrs)
        p_mock3 = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        p_mock3.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt has been modified locally')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_untracked(self, mock_subproc_popen):
        """
        Checks if ability to detected files which have not been checked in, is operational
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value'
                 : (PARENT_DIRECTORY, '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt has been not been checked in')
        self.assertRaises(Exception, git_utils.get_git_file_info, 'X/:somethingnottrue')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_dirty(self, mock_subproc_popen):
        """
        Checks for functionality of dirty repo detection.
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock5 = mock.Mock()
        p_mock5.configure_mock(**attrs)
        attrs = {'communicate.return_value'
                 : (PARENT_DIRECTORY, '')}
        p_mock6 = mock.Mock()
        p_mock6.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock7 = mock.Mock()
        p_mock7.configure_mock(**attrs)
        attrs = {'communicate.return_value'
                 : (PARENT_DIRECTORY, '')}
        p_mock8 = mock.Mock()
        p_mock8.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4,
                                          p_mock5, p_mock6, p_mock7, p_mock8]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt is a dirty repo')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_dirty_untr(self, mock_subproc_popen):
        """
        checks for correct detection of dirty repo with untracked.
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        p_mock5 = mock.Mock()
        p_mock5.configure_mock(**attrs)
        p_mock6 = mock.Mock()
        p_mock6.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')} #get_untracked
        p_mock7 = mock.Mock()
        p_mock7.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock8 = mock.Mock()
        p_mock8.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4,
                                          p_mock5, p_mock6, p_mock7, p_mock8]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt is a dirty repo')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_noaction(self, mock_subproc_popen):
        """
        Checks that detection of a file with no extraordinary status information is correct
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt is up to date')


#'<hash>, <date modified>, <author>'
    @requirements(['#0102'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_info(self, mock_subproc_popen):
        """
        Checks that hash info is detected correclty
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        attrs = {'communicate.return_value' : ('somehash, Wed Feb 3 17:32:12 2016 -0800,'
                                               ' patrickcarlson', '')}
        p_mock1 = mock.Mock()
        p_mock1.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1]
        qaobject = Interface()
        result = qaobject.ask("What is the deal with <nose2.cfg>?")
        self.assertEqual(result, 'somehash, Wed Feb 3 17:32:12 2016 -0800, patrickcarlson')

    @requirements(['#0103'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_branch_info(self, mock_subproc_popen):
        """
        Checks that branch info is detected correctly.
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        attrs = {'communicate.return_value' : ('master', '')}
        p_mock1 = mock.Mock()
        p_mock1.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock1
        qaobject = Interface()
        result = qaobject.ask("What branch is <nose2.cfg>?")
        self.assertEqual(result, 'master')

    @requirements(['#0104'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_url(self, mock_subproc_popen):
        """
        Checks that appropiate url is returned
        :param mock_subproc_popen: Function who's return is mocked
        :return:
        """
        attrs = {'communicate.return_value' : ('https://github.com/OregonTech/PatrickC', '')}
        p_mock1 = mock.Mock()
        p_mock1.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock1
        qaobject = Interface()
        result = qaobject.ask("Where did <nose2.cfg> come from?")
        self.assertEqual(result, 'https://github.com/OregonTech/PatrickC')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_repo_coverage(self, mock_subproc_popen):
        """
        Checks that Assertion is thrown correctly.
        :param mock_subproc_popen:
        :return:
        """
        attrs = {'communicate.return_value' : (__file__, '')}
        p_mock = mock.Mock()
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        something = git_utils.get_repo_root('ProjectRequirements.txt')
        self.assertEqual(something, __file__)
