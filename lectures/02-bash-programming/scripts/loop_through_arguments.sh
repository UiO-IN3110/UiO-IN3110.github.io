#!/bin/bash

echo "You start with $# positional parameters"

# Loop until all parameters are used up
while [ "$1" != "" ]; do
    echo "The next parameter is $1, $# remaining"

    # Shift all the parameters down by one
    shift
done
