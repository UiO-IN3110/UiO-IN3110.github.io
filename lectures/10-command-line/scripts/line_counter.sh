#!/bin/bash
filename="text.txt"
declare -i count; count=0

echo "Start counting..."
# loop over all lines of  file
while read p;
do
    # increase line counter
    ((count++))
done < $filename
echo "done"

echo "Number of lines in $file: $count"
