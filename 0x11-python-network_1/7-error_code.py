#!/usr/bin/python3
"""This script gets the status code of a request"""
import requests
from sys import argv


def get_request_status(url: str):
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    get_request_status(argv[1])
