#!/bin/bash

if [ "`date +%R`" == "tirsdag" ]; then
   echo "Starting backup."
else
   echo "No backup today."
fi        
