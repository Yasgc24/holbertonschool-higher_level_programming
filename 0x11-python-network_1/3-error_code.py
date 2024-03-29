#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8)"""
from urllib import request
from sys import argv
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
