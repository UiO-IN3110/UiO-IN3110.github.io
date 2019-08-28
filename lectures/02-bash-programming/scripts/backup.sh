#!/bin/bash

if [ "`date +%R`" == "onsdag" ]; then
   echo "Starting backup."
else
   echo "No backup today."
fi        
