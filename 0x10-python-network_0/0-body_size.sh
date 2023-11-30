#!/usr/bin/env bash
# shows the bytes of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2

