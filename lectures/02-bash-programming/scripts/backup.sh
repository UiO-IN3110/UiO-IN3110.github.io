#!/bin/bash -x

if [ "`date +%A`" == "onsdag" ]; then
   echo "Starting backup."
else
   echo "No backup today."
fi        
