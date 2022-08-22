#! /bin/bash

myvar=$(curl -s https://wttr.in/Oslo | head -7)

loc=$(echo $myvar | cut -d '\' -f1 | cut -d ":" -f2)
desc=$(echo $myvar | cut -d '/' -f2 | cut -d "." -f1)
deg=$(echo $myvar  | cut -d "." -f3  | cut -d "(" -f1 )

echo Location: $loc
echo Description: $desc
echo Degrees: $deg


