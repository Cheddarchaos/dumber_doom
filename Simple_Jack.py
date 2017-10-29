import random
import requests
import json
import recreationalnuclearbombs
import move_toward
import math


portvariable = 6001
while True:

    listobjects = requests.get("http://localhost:%s/api/world/objects" % portvariable)
    list_players = requests.get("http://localhost:%s/api/players" % portvariable)
    print(list_players)
    playerdata = list_players.text
    list_pl = json.loads(playerdata)

    gooddata = listobjects.text
    list_obj = json.loads(gooddata)

    recreationalnuclearbombs.Aimbot('Player', list_pl, 1)

    x, y = move_toward.closest_target(move_toward.choose_dest(), list_obj)

    move_toward.move_toward(x,y)
    requests.post("http://localhost:%s/api/player/actions" % portvariable, json={'type': 'use'})



