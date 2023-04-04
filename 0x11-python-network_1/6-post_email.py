#!/usr/bin/python3
"""This script sends a POST request"""
import requests
from sys import argv


def get_request(url: str, email_arg: str):
    payload = {"email": email_arg}
    req = requests.post(url, data=payload)
    print(req.text)


if __name__ == "__main__":
    get_request(argv[1], argv[2])
