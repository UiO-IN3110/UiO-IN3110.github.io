#!/bin/bash

curl -s http://www.yr.no/place/Norway/Oslo/Oslo/Oslo/ | grep -m 1 "temperature" | cut -d"\"" -f4
