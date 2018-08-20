#!/bin/bash

while [ $# -gt 0 ]  # $# = no of command-line args.
do
    option=$1; # load command-line arg into option
    shift;       # eat currently first command-line arg
    case "$option" in
        -m)
            m=$1; shift; ;;  # ;; indicates end of case
        -b)
            b=$1; shift; ;;
        *)
            echo "$0: invalid option \"$option\""; exit ;;
    esac
done

echo "Command line arguments:"
[ -n "$m" ] && echo "m=$m"
[ -n "$b" ] && echo "b=$b"
