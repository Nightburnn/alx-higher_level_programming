#!/usr/bin/python3
"""This script communicates with an API and gets a JSON formatted response"""
import requests
from sys import argv


def get_request_status(letter: str):
    payload = {}
    payload["q"] = letter

    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=payload)

    try:
        resp_dict = req.json()
        if resp_dict:
            print("[{}] {}".format(resp_dict.get("id"), resp_dict.get("name")))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    try:
        letter = argv[1]
    except IndexError:
        letter = ""
    finally:
        get_request_status(letter)
