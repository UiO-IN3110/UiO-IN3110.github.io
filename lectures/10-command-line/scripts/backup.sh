#!/bin/bash -x

if [ "$(date +%a)" == "onsdag" ]; then
   echo "Starting backup."
else
   echo "No backup today."
fi
