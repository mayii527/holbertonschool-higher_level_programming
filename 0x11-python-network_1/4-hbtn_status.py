#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
use the package requests.
"""
import requests


if __name__ == "__main__":
    resp: requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
