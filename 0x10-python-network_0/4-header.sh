#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL
curl -s --header X-School-User-Id:98 "$1"
