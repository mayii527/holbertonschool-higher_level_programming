#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
use the package requests.
"""
import requests


if __name__ == "__main__":
    res: requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
