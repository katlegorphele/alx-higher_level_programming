#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to
the URL and displays value of X-Request-Id variable
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
