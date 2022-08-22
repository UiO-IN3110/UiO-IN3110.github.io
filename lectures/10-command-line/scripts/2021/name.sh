#! /bin/bash

name=$1
age=$2

declare -i old_age
declare -i number

old_age=$age+10

number=$(echo $name | wc -c)-1

echo $name is $age years old. He has $number letters in his name.


oa=$(echo $age+10 | bc)
echo $name is $age years old. He has $number letters in his name. 

echo In 10 years he will be $old_age years old


if [ $old_age -gt 50 ]; then
    echo $name will be old in 10 years
    
else
    echo $name is still young in 10 years

fi
