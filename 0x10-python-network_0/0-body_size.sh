#!/bin/bash
# shows the bytes of the response
curl -sI"$1" | grep "Content-Length" | cut -d " " -f2
