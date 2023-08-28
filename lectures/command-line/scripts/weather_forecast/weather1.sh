#!/bin/bash

curl -s https://www.yr.no/place/Norway/Oslo/Oslo/Oslo/ | \
grep "temperature" | \
cut -d"\"" -f4 | \
head -n 1 | \
cowsay
