#!/bin/bash

op=$1
shift
case "$op" in
    S)
	sum=0
	for n in $@
	do
	    sum=$((sum+n))
	done
	echo $sum
	;;
    
    P)
	prod=1
	for n in $@
	do
	    prod=$((prod*n))
	done
	echo $prod	
	;;
    
    M)
	max=$1
	shift
	for n in $@
	do
	    if [ $n -gt $max ]; then
	       max=$n
	    fi
	done
	echo $max
	;;
    
    m)
	min=$1
	shift
	for n in $@
	do
	    if [ $n -lt $min ]; then
	       min=$n
	    fi
	done
	echo $min
	;;
    
    *)
	echo "What does $op mean?;"
	;;
esac
