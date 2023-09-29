#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(Request(argv[1]))as response:
        response_id = response.headers.get("X-Request-Id")
        print(response_id)
