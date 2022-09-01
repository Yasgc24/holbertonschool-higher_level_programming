#!/usr/bin/python3
"""script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response."""
from platform import architecture
from sys import argv
from urllib import response
import requests


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {"email": email}

    response = requests.post(url, value)
    print(response.text)
