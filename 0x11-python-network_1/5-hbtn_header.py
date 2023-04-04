#!/usr/bin/python3
"""This script sends a get request for a header"""
import requests
from sys import argv


def get_request(url: str):
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_request(argv[1])
