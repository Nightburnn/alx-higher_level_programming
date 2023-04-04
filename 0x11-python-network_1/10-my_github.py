#!/usr/bin/python3
"""This script communicates with an API and gets the github ID"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def get_id_from_githubapi(username: str, password: str):
    """The password is the personal access token"""

    basic_auth = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user"

    """The github api allows the 'Authorization' header
        be specified in the authentication of user access to
        private information
    """
    headers = {"Authorization": "Bearer {}".format(password)}
    req = requests.get(url, headers=headers, auth=basic_auth)

    resp_dict = req.json()
    print(resp_dict.get("id"))


if __name__ == "__main__":
    try:
        username = argv[1]
        token = argv[2]
        get_id_from_githubapi(username, token)
    except IndexError:
        pass
