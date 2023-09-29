#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the
header of the response.
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}
    data = urlencode(values).encode("ascii")

    with urlopen(Request(url, data))as response:
        print(response.read().decode("utf-8", "replace"))
