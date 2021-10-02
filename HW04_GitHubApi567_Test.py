"""
Updated Sept 18, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Viyeta Kansara

"""

import unittest

from HW04_GitHubApi567 import get_repo_commits


class GitHubApi567(unittest.TestCase):

    def test0_repos(self):
        repos = get_repo_commits('richkempinski')
        self.assertIn('helloworld', repos)

    def test1_repos(self):
        self.assertRaises(ValueError, get_repo_commits, 'some_random_invalid_user')

    def test1_commits(self):
        self.assertEqual(6, get_repo_commits("richkempinski")['helloworld'])

    def test2_commits(self):
        self.assertEqual(0, get_repo_commits("Viyeta")['for-commit-check'])

    def test3_commits(self):
        self.assertEqual(9, get_repo_commits("Viyeta")['Triangle-SSW567'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
