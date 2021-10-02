"""
Updated Oct 01, 2021

The primary goal of this file is to retrieve a user's repositories and the commits of a repository.

@author: Viyeta Kansara

"""
from typing import Dict, List

import requests
import json

from requests import Response


def get_repos(github_id: str) -> List[str]:
    # check valid non empty string
    url = "https://api.github.com/users/" + github_id + "/repos"
    response = http_get_request(url)
    # response = requests.get("https://api.github.com/users/" + github_id + "/repos")
    if not response.json():
        raise ValueError("Account has no repos")
    repos = []
    response_json = json.loads(response.text)
    # check empty response (no repos)
    for repo in response_json:
        repos.append(repo['name'])
    return repos


def get_repo_commits(github_id: str) -> Dict[str, int]:
    # check valid non empty string
    repos = get_repos(github_id)
    repo_commits_dict = {}
    for repo in repos:
        url = "https://api.github.com/repos/" + github_id + "/" + repo + "/commits"
        response = http_get_request(url)
        # response = requests.get("https://api.github.com/repos/" + github_id + "/" + repo + "/commits")
        response_json = json.loads(response.text)
        # check for empty response
        if response.status_code == 409:
            repo_commits_dict[repo] = 0
        else:
            repo_commits_dict[repo] = len(response_json)
    return repo_commits_dict


def http_get_request(url: str) -> Response:
    response = requests.get(url)
    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        raise ValueError("Page not found")
    elif response.status_code == 400:
        raise ValueError("Invalid request")
    elif response.status_code == 409 and json.loads(response.text)['message'] == 'Git Repository is empty.':
        return response
    else:
        raise ValueError("Unknown error")


def main():
    """ main function"""
    user_id = input('Enter Your GitHub username:')

    github_id(user_id)


if __name__ == "__main__":
    main()