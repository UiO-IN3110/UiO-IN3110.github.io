subl game_server1.py
python3 game_server1.py
killall subl

read -p "Press enter to open version 2"
subl --new-window templates/select2.html game_server2.py 
python3 game_server2.py
killall subl

read -p "Press enter to open version 3"
subl --new-window templates/reselect3.html game_server3.py
python3 game_server3.py
killall subl

read -p "Press enter to open version 4"
subl --new-window templates/select4.html templates/reselect4.html game_server4.py
python3 game_server4.py
killall subl

read -p "Press enter to open version 5"
subl --new-window templates/final.html game_server5.py
python3 game_server5.py
killall subl

read -p "Press enter to open version 6"
subl --new-window game_server6.py 
python3 game_server6.py
killall subl

read -p "Press enter to open version 7"
subl --new-window templates/select7.html templates/reselect7.html templates/final7.html templates/layout7.html game_server7.py
python3 game_server7.py
killall subl
