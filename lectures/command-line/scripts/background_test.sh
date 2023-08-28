#!/bin/bash
sleep 1 && echo "First sleep finished" &
sleep 2 && echo "Second sleep finished" &
sleep 3 && echo "Third sleep finished" &
wait
echo "All sleeps finished"
