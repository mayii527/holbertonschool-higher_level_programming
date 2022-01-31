#!/usr/bin/python3
"""
Write a Python script that fetches
https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        print(res)
