#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    URL = argv[1]
    email = argv[2]
    value = {"email": email}
    query = parse.urlencode(value)
    data = query.encode("utf-8")
    with request.urlopen(URL, data) as response:
        print(response.read().decode("utf-8"))
