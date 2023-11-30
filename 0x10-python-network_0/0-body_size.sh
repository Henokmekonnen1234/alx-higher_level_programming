#!/usr/bin/env bash
 # shows the bytes of the response
curl -w "%{size_download\n" "$1"
