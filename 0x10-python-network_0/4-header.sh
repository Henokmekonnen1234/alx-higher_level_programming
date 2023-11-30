#!/bin/bash
# this will set header variable to the give value and display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
