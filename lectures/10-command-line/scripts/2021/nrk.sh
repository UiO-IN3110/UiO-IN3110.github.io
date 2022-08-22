url=https://www.nrk.no/

curl -s $url | grep "newsfeed__message-title" | cut -d '>' -f2 | cut -d '<' -f1

