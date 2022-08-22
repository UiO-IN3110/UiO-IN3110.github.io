#! /bin/bash

message=$@
dato=$(date '+%Y-%m-%d %H:%M:%S')

echo $dato - $message >> journal.txt
