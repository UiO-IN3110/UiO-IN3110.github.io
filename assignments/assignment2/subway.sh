#!/bin/bash


## list of route names servicing the stops we use sorted into 'directions'
west_route_names=("\"Sognsvann\"" 
		  "\"Vestli via Storo\""
		  "\"Ringen via Storo\"")

east_route_names=("\"Bergkrystallen via Majorstuen\""
		  "\"Ringen via Majorstuen\""
		  "\"Ryen\""
		  "\"Vestli via Majorstuen\""
		  "\"Vestli\"")

all_route_names=( "${west_route_names[@]}" )
all_route_names+=( "${east_route_names[@]}" )
tmp_fn="ruter_tmp.html"		# file for holding wget data

while [ $# -gt 0 ]
do
    op=$1
    shift
    case "$op" in
	--W)
	    valid_names=( "${west_route_names[@]}" )
	    ;;
	
	--E)
	    valid_names=( "${east_route_names[@]}" )
	    ;;
	
	*)
	    if [ -z "$valid_names" ]; then # check tjat no --W/E flag was parsed already
		valid_names=( "${all_route_names[@]}" )
	    fi
	    
	    case "$op" in
	    Blindern)
		echo "Fetching times from Blindern"

		wget -q https://ruter.no/reiseplanlegger/Stoppested/\(3010360\)Blindern%20%5bT-bane%5d%20\(Oslo\)/Avganger/#st:1,sp:0,bp:0 -O $tmp_fn
		;;

	    Nydalen)
		echo "Fetching times from Nydalen"

		wget -q https://ruter.no/reiseplanlegger/Stoppested/\(3012130\)Nydalen%20%5bT-bane%5d%20\(Oslo\)/Avganger/#st:1,sp:0,bp:0 -O $tmp_fn
		;;

	    Forskningsparken)
		echo "Fetching times from Forskningsparken"
		wget -q https://ruter.no/reiseplanlegger/Stoppested/\(3010370\)Forskningsparken%20%5bT-bane%5d%20\(Oslo\)/Avganger/#st:1,sp:0,bp:0 -O $tmp_fn
		;;
	    *)
		echo "Sorry, I don't know that stop"
		exit
		;;
	    esac
    esac
done

if [ ! -f "$tmp_fn" ]; then # check that some station was actually supplied
    echo "Please specify a stop"
    exit
fi

dict=$(grep AlightingAllowed $tmp_fn) # huge single line containing all route information

printf "%-40s: %s\n\n" "Current time" $(date +%H:%M)

for name in "${valid_names[@]}";
do
    len=${#dict}
    s=${dict#*$name}
    
    if [ "$len" -eq ${#s} ]; then 
	continue # if nothing was removed, no routes of this name is departing
    fi
    
    s=${s#*departureTime\":\"}
    time=${s%%\",*}
    printf "%-40s: %s\n" "${name:1:-1}" "$time"
done

rm $tmp_fn
