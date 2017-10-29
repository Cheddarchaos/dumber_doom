import random
import requests
import json
import recreationalnuclearbombs
import move_toward
import math

j = 0
while True:
    listobjects = requests.get("http://localhost:6001/api/world/objects")
    list_players = requests.get("http://localhost:6001/api/world/players")

    playerdata = list_players.text
    list_pl = json.loads(playerdata)

    gooddata = listobjects.text
    list_obj = json.loads(gooddata)

    recreationalnuclearbombs.Aimbot('Player', list_pl, 1)

    x, y = move_toward.closest_target(move_toward.choose_dest(), list_obj)

    move_toward.move_toward(x,y)

    j += 1
    if j > 30:
        break