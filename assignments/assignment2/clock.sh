#!/bin/bash


while true
do
    printf "\033c" # basically clear
    if [ "$1" = "--AMPM" ]; then
	if [ "$(date +%H)" -gt "11" ]; then
	    date +%rPM
	else
	    date +%rAM
	fi
    else
	date +%H:%M:%S
    fi
    sleep 1.0s
done
