#!/bin/bash
# http response size in bytes
curl -s "$1" | wc -c
