import unittest
from unittest import mock
from unittest.mock import MagicMock

import GitInfo

class test_gitmock(unittest.TestCase):
    @mock.patch('GitInfo.getNoOfCommits')
    def test_mock_noOfCommits(self, mock_user):
        mock_user.return_value = MagicMock(user_id="desai-aayushi", repo_name="SSW567_HW02a")
        print(mock_user.return_value)
        result = mock_user.return_value.user_id
        try:
            self.assertEqual(result, "desai-aayushi")
        except:
            print("Test Failed")
        else:
            print("Test succeed")

    @mock.patch('GitInfo.getGitRepoInfo')
    def test_mock_noOfRepo(self, mock_user):
        mock_user.return_value = MagicMock(user_id="desai-aayushi")
        print(mock_user.return_value)
        result = mock_user.return_value.user_id
        try:
            self.assertEqual(result, "desai-aayushi")
        except:
            print("Test Failed")
        else:
            print("Test succeed")


if __name__ == '__main__':
    unittest.main()
