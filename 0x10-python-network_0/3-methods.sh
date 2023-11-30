#!/bin/bash
#this will show all http methods that the server will accept
curl -sIL "$1" -X OPTIONS | grep -i Allow | cut -d " " -f2
