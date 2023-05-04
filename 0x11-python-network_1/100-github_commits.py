#!/usr/bin/python3

"""
Script that list 10 commits (from the most recent to oldest)
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print(
            "{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name"),
            )
        )
