from source.main import Interface
from source import git_utils
from unittest import TestCase
from test.plugins.ReqTracer import requirements
from mock import mock, Mock, patch, MagicMock

class gitutilstests(TestCase):

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_file_path_abs_bool(self, mock_subproc_popen):
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('', ' ')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the nose2.cfg in the repo?")
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_file_path_exists_bool(self, mock_subproc_popen):
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('Output', 'Error')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the ProjectRequirements.txt in the repo?")
        self.assertEqual(result, 'Yes')


    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_file_path_dne_bool(self, mock_subproc_popen):
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the E:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab in the repo?")
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_util_file_path_difffiles_bool(self, mock_subproc_popen):
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('C:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab\didntcommit.txt', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("Is the didntcommit.txt in the repo?")
        self.assertEqual(result, 'No')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_status_localmod(self, mock_subproc_popen):
        p_mock = mock.Mock()
        attrs = {'communicate.return_value' : ('C:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab\didntcommit.txt', '')}
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt has been modified locally')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_status_untracked(self, mock_subproc_popen):
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('C:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab' , '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt has been not been checked in')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_status_dirty(self, mock_subproc_popen):
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('' , '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock5 = mock.Mock()
        p_mock5.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('C:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab', '')}
        p_mock6 = mock.Mock()
        p_mock6.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock7 = mock.Mock()
        p_mock7.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('C:\Users\Pat\Documents\School\CST236\PatrickC\cst236_lab', '')}
        p_mock8 = mock.Mock()
        p_mock8.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4, p_mock5, p_mock6, p_mock7, p_mock8]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt is a dirty repo')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_status_dirty_hasuntracked(self, mock_subproc_popen):
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('' , '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}  #has_diff_files
        p_mock5 = mock.Mock()
        p_mock5.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')} #staged
        p_mock6 = mock.Mock()
        p_mock6.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('didntcommit.txt', '')} #get_untracked
        p_mock7 = mock.Mock()
        p_mock7.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock8 = mock.Mock()
        p_mock8.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4, p_mock5, p_mock6, p_mock7,p_mock8]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt is a dirty repo')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_status_noaction(self, mock_subproc_popen):
        p_mock1 = mock.Mock()
        attrs = {'communicate.return_value' : ('', '')}
        p_mock1.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock2 = mock.Mock()
        p_mock2.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock3 = mock.Mock()
        p_mock3.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock4 = mock.Mock()
        p_mock4.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock5 = mock.Mock()
        p_mock5.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock6 = mock.Mock()
        p_mock6.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock7 = mock.Mock()
        p_mock7.configure_mock(**attrs)
        attrs = {'communicate.return_value' : ('', '')}
        p_mock8 = mock.Mock()
        p_mock8.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1, p_mock2, p_mock3, p_mock4, p_mock5, p_mock6, p_mock7, p_mock8]
        qaobject = Interface()
        result = qaobject.ask("What is the status of <didntcommit.txt>?")
        self.assertEqual(result, 'didntcommit.txt is up to date')


#'<hash>, <date modified>, <author>'
    @requirements(['#0102'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_path_info(self, mock_subproc_popen):
        attrs = {'communicate.return_value' : ('somehash, Wed Feb 3 17:32:12 2016 -0800, patrickcarlson', '')}
        p_mock1 = mock.Mock()
        p_mock1.configure_mock(**attrs)
        mock_subproc_popen.side_effect = [p_mock1]
        qaobject = Interface()
        result = qaobject.ask("What is the deal with <nose2.cfg>?")
        self.assertEqual(result, 'somehash, Wed Feb 3 17:32:12 2016 -0800, patrickcarlson')

    @requirements(['#0103'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_branch_info(self, mock_subproc_popen):
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
        attrs = {'communicate.return_value' : ('https://github.com/OregonTech/PatrickC', '')}
        p_mock1 = mock.Mock()
        p_mock1.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock1
        qaobject = Interface()
        result = qaobject.ask("Where did <nose2.cfg> come from?")
        self.assertEqual(result, 'https://github.com/OregonTech/PatrickC')

    @requirements(['#0101'])
    @patch('source.git_utils.subprocess.Popen')
    def test_git_utils_get_repo_completeness(self, mock_subproc_popen):
        attrs = {'communicate.return_value' : ('C:/Users/Pat/Documents/School/CST236/PatrickC', '')}
        p_mock = mock.Mock()
        p_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = p_mock
        something = git_utils.get_repo_root('ProjectRequirements.txt')
        self.assertEqual(something, 'C:\\Users\\Pat\\Documents\\School\\CST236\\PatrickC')

    @requirements(['#0101'])
    def test_git_utils_check_valid_path_exception(self):
        self.assertRaises(Exception, git_utils.get_git_file_info, 'X/:somethingnottrue')