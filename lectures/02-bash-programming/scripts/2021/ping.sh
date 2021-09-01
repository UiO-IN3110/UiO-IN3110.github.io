#! /bin/bash

ping google.com -c 1 &> /dev/null

if [ $? -gt 0 ]; then
    echo Internet not connected
else
    echo Internet connected
fi



# IN TERMINAL
# $ watch -n 1 ./ping.sh
