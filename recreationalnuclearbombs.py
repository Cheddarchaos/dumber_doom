import requests
import json
import math
import random
import aim_at_point


def Aimbot(target, list_pl, shots):

    from pprint import pprint as pp

    connect = "http://localhost:6001/api/player"

    r = requests.get(connect)

    Xtarget = []
    Ytarget = []
    Targetlist = []

    px = r.text
    playerid = (json.loads(px))["id"]
    print(list_pl)
    for entity in list_pl:
        if entity["type"] == target and not entity["isConsolePlayer"]:
            Targetlist.append(entity["id"])
            tempo = (entity["position"])
            Xtarget.append(tempo["x"])
            Ytarget.append(tempo["y"])
    if len(Xtarget) > 0:
        minX = Xtarget[0]
        minY = Ytarget[0]
        minangle = aim_at_point.find_angle(minX, minY)
        for i in range(len(Xtarget)):
            angle = aim_at_point.find_angle(Xtarget[i],Ytarget[i])
            if angle < minangle:
                minX = Xtarget[i]
                minY = Ytarget[i]

        aim_at_point.aim_point(minX,minY)


        for jeff in range(shots):
            for elt in Targetlist:
                derpstring = 'http://localhost:6001/api/world/los/%s/%s' % (playerid,elt)
                lineos = requests.get(derpstring)
                memes = lineos.text
                lineos2 = json.loads(memes)
                if "los" in lineos2:
                    if lineos2["los"]:
                        requests.post('http://localhost:6001/api/player/actions', json={"type": "shoot","amount": 3})

""""
for i in range(2):

    Aimbot("Barrel",list_obj)
"""