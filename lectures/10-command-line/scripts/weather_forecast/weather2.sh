#!/bin/bash

function city_url {
	if [ $1 == "Oslo" ]; then
		url="https://www.yr.no/place/Norway/Oslo/Oslo/Oslo/"
	fi
}

city_url "Oslo"

echo $url

curl -s https://www.yr.no/place/Norway/Oslo/Oslo/Oslo/ | \
grep "temperature" | \
cut -d"\"" -f4 | \
head -n 1 | \
cowsay