#!/bin/bash
# this will set header variable to the give value and display the body of the response
curl -H "X-School-User-Id: 98" "$1"
