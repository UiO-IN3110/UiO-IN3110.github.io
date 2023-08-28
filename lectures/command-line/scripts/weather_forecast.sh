#!/bin/bash

curl -s https://www.yr.no/place/Norway/Oslo/Oslo/Oslo/ | grep -m 1 "temperature" | cut -d"\"" -f4 | cowsay
