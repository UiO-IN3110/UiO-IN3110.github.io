sleep 1 && echo "Sleep 1s finished" &
sleep 2 && echo "Sleep 2s finished" &
sleep 3 && echo "Sleep 3s finished" &
wait
echo "All sleeps finished"
