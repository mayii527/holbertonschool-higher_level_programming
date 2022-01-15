#!/bin/bash
# that takes in a URL, sends a POST request to the passed URL
curl -sX POST --data "email=test@gmail.com&subject=I will always be here for PLD" $1
