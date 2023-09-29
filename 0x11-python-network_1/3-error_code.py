#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the
URL and displays the body of the response
with managing  exceptions
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(Request(url))as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
