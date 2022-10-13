import unittest
from GitInfo import getGitRepoInfo, getNoOfCommits


class TestGitInfo(unittest.TestCase):
    def test_userId(self):
        self.assertEqual(getGitRepoInfo(111111), "User ID is not valid")

    def test_NoOfCommits(self):
        self.assertEqual(getNoOfCommits("desai-aayushi", "SSW567_HW02a"), 8)

    def test_gitRepos(self):
        self.assertListEqual(getGitRepoInfo("desai-aayushi"),
                             ["dbmsproject", "LT_Project", "SSW567_HW00_HelloWorld", "SSW567_HW02a","SSW567_HW04a","SSW567_HW05"])


if __name__ == '__main__':
    unittest.main()
