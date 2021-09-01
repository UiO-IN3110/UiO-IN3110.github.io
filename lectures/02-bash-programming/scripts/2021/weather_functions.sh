#! /bin/bash

function geturl {
    # function args are referred to as $1 $2 etc
    if [ $1 == "Oslo" ]; then
        url=https://www.yr.no/en/forecast/daily-table/1-72837/Norway/Oslo/Oslo/Oslo
    elif [ $1 == "Bergen" ]; then
        url=https://www.yr.no/en/forecast/daily-table/1-92416/Norway/Vestland/Bergen/Bergen
    elif [ $1 == "Stavanger" ]; then
        url=https://www.yr.no/en/forecast/daily-table/1-15183/Norway/Rogaland/Stavanger/Stavanger
    else
        url="No such city"
    fi   
}

geturl Oslo

echo $url
    
    
