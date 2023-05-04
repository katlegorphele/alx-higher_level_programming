#!/usr/bin/python3

"""
Script that takes in URL and email, sends POST request 
to passed URL with email as parameter, displays body of 
response decoded in utf-8
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
