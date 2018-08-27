#!/bin/bash

# run_and_test.sh 
echo "Running the command $@"
$@

if [ "$?" == "0" ]; then      # $? returns 0 if the last command was success
    echo "Command succeeded - exciting."
else
    echo "Oops, there was an error."
fi
