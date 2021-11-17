#! /bin/bash

curl -s https://pent.no/59.91273,10.74609 | grep storm.no | head -n 1 | cut -d '"' -f1




#curl -s https://pent.no/59.91273,10.74609 | grep YR | head -n 1
