sleep 1 && echo "First sleep finished" &
sleep 1 && echo "Second sleep finished" &
sleep 1 && echo "Third sleep finished" &
wait
echo "All sleeps finished"
