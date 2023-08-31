#!/bin/bash
#script that takes in a URL and displays all HTTP methods
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
