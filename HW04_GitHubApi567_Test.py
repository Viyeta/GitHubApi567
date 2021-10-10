"""
Updated Oct 09, 2021
The primary goal of this file is to demonstrate a simple unittest implementation with mocked response
JSON response files are kept in json directory and response structure is checked against them
The purpose is to validate according to the actual response we get from Github APIs

@author: Viyeta Kansara

"""
import os
import unittest
from unittest import mock

from HW04_GitHubApi567 import get_repo_commits


def mocked_requests_get(*args, **kwargs):

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = json_data

        def json(self):
            return self.json_data

    root_dir = os.path.dirname(__file__)
    with open(os.path.join(root_dir, "json/Viyeta_repos.json"), "r") as file:
        data = file.read()
    if args[0] == 'https://api.github.com/users/Viyeta/repos':
        return MockResponse(data, 200)

    splits = args[0].split('/')
    if len(splits) == 7 and splits[3] == 'repos':
        with open(os.path.join(root_dir, "json\\Viyeta_" + splits[5] + "_commits.json"), "r") as file2:
            data2 = file2.read()
            return MockResponse(data2, 200)

    return MockResponse(None, 404)


class GitHubApi567(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test0_repos(self, mock_get):
        repos = get_repo_commits('Viyeta')
        self.assertIn('for-commit-check', repos)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test1_repos(self, mock_get):
        self.assertRaises(ValueError, get_repo_commits, 'some_random_invalid_user')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test2_commits(self, mock_get):
        self.assertEqual(2, get_repo_commits("Viyeta")['for-commit-check'])

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test3_commits(self, mock_get):
        self.assertEqual(9, get_repo_commits("Viyeta")['Triangle-SSW567'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
