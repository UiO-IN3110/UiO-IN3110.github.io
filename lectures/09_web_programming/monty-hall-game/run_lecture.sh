read -p "Press enter to open version 1"
subl game_server1.py
read -p "Press enter to run version 1"
python game_server1.py

read -p "Press enter to open version 2"
subl --new-window templates/select2.html game_server2.py 
read -p "Press enter to run version 2"
python game_server2.py

read -p "Press enter to open version 3"
subl --new-window templates/reselect3.html game_server3.py
read -p "Press enter to run version 3"
python game_server3.py

read -p "Press enter to open version 4"
subl --new-window templates/select4.html templates/reselect4.html game_server4.py
read -p "Press enter to run version 4"
python game_server4.py

read -p "Press enter to open version 5"
subl --new-window final.html game_server5.py
read -p "Press enter to run version 5"
python game_server5.py

read -p "Press enter to open version 6"
subl --new-window game_server6.py 
read -p "Press enter to run version 6"
python game_server6.py

read -p "Press enter to open version 7"
subl --new-window templates/select7.html templates/reselect7.html templates/final7.html templates/layout.html game_server7.py
read -p "Press enter to run version 7"
python game_server7.py
