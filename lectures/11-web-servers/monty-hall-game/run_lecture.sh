#!/bin/bash

editor=${editor:-nova}
$editor game_server1.py
python3 game_server1.py

read -p "Press enter to open version 2"
$editor templates/select2.html game_server2.py
python3 game_server2.py

read -p "Press enter to open version 3"
$editor templates/reselect3.html game_server3.py
python3 game_server3.py

read -p "Press enter to open version 4"
novv templates/select4.html templates/reselect4.html game_server4.py
python3 game_server4.py

read -p "Press enter to open version 5"
$editor templates/final5.html game_server5.py
python3 game_server5.py

read -p "Press enter to open version 6"
$editor game_server6.py
python3 game_server6.py

read -p "Press enter to open version 7"
$editor templates/select7.html templates/reselect7.html templates/final7.html templates/layout7.html game_server7.py
python3 game_server7.py
