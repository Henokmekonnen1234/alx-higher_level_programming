#!/bin/bash
#this will show all http methods that the server will accept
curl -sI "$1" | grep -i Allow | cut -d " " -f2
