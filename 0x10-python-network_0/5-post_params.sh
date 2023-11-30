#!/bin/bash
# this will send request with post and variabels
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
