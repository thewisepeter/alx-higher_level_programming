#!/bin/bash
#script that takes in a URL, sends a request to that URL, displays results
curl -s  "$1" | wc -c
