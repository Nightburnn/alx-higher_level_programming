#!/usr/bin/python3
"""This script makes a request to the url and gets a response"""
from urllib.request import urlopen, Request
from urllib.error import URLError


def get_body_decode():
    try:
        req = Request("https://alx-intranet.hbtn.io/status")
        with urlopen(req) as response:
            body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)


if __name__ == "__main__":
    get_body_decode()
