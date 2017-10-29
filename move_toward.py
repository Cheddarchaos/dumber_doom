
import requests
import aim_at_point
import json
import math
import pprint as pp

orX = -1304
orY = -590

connect = "http://localhost:6001/api"

r = requests.get(connect+ "/player")

pos = r.json()["position"]

print(str(pos))

#moves a small distance towards a target x, y
def move_toward(x,y):
    r = requests.get(connect + "/player")

    px = r.text
    playerid = (json.loads(px))["id"]

    dx = x - r.json()["position"]["x"]
    dy = y - r.json()["position"]["y"]

    pl_angle = r.json()["angle"]
    tar_angle = aim_at_point.find_angle(x, y)
    if tar_angle < 0:
        tar_angle += 360

    d_angle = tar_angle - pl_angle

    if d_angle < 0:
        d_angle += 360

    d_angle = (d_angle*math.pi)/180
    dist = 10

    d_forward = math.cos(d_angle)*dist

    d_left = math.sin(d_angle)*dist


    if d_forward > 0:
        requests.post(connect + "/player/actions", json={'type': 'forward', 'amount': d_forward})
    else:
        requests.post(connect + "/player/actions", json={'type': 'backward', 'amount': abs(d_forward)})

    if d_left > 0:
        requests.post(connect + "/player/actions", json={'type': 'strafe-left', 'amount': d_left})
    else:
        requests.post(connect + "/player/actions", json={'type': 'strafe-right', 'amount': abs(d_left)})


def closest_target(target, list_obj):
    connect = "http://localhost:6001/api/player"

    r = requests.get(connect)
    angle1 = r.json()["angle"]
    pos = r.json()["position"]

    if target == None:
        angle = aim_at_point.find_angle(orX,orY)
        dx = orX - r.json()["position"]["x"]
        dy = orY - r.json()["position"]["y"]
        dist_or = math.sqrt((dx*dx)+(dy*dy))
        x = math.sin(angle - 10)*dist_or
        y = math.cos(angle - 10)*dist_or
        return x, y

    Targetlist = []
    k = 0
    for entity in list_obj:
        if entity["type"] == target:
            Targetlist.append(entity["id"])
            tempo = (entity["position"])
            if k == 0:
                minX = tempo["x"]
                minY = tempo["y"]

                dx = minX - r.json()["position"]["x"]
                dy = minY - r.json()["position"]["y"]

                dist_min = math.sqrt(dx*dx + dy*dy)
            k = 1
            dx = tempo["x"] - r.json()["position"]["x"]
            dy = tempo["y"] - r.json()["position"]["y"]

            dist = math.sqrt(dx*dx + dy*dy)

            if dist < dist_min:
                minX = tempo["x"]
                minY = tempo["y"]
    if k == 1:
        return minX, minY
    else:
        angle = aim_at_point.find_angle(orX, orY)
        dx = orX - r.json()["position"]["x"]
        dy = orY - r.json()["position"]["y"]
        dist_or = math.sqrt((dx * dx) + (dy * dy))
        x = math.cos(angle - 10) * dist_or
        y = math.sin(angle - 10) * dist_or
        return x, y

def choose_dest():
    connect = "http://localhost:6001/api"
    listobjects = requests.get(connect + "/world/objects")
    gooddata = listobjects.text
    list_obj = json.loads(gooddata)
    r = requests.get(connect + "/player")

    if (r.json()["ammo"]["Shells"] == 0) and (r.json()["ammo"]["Bullets"] == 0):
        if closest_target('Shotgun shells', list_obj) != None and closest_target('Ammo clip', list_obj) != None:
            return 'Player'

    if r.json()["ammo"]["Shells"] < 10:
        if closest_target('Shotgun shells', list_obj) != None:
            print("Shotgun shells")
            return 'Shotgun shells'


    if not r.json()["weapons"]["Shotgun"]:
        if closest_target('Shotgun', list_obj) != None:
            print('Shotgun')
            return 'Shotgun'

    if r.json()["ammo"]["Bullets"] < 15:
        if closest_target('Ammo clip', list_obj) != None:
            print('Ammo clip')
            return 'Ammo clip'

    if r.json()["armor"] < 50:
        if closest_target('armor', list_obj) != None:
            print("armor")
            return 'Green armor 100%'

    if r.json()["health"] < 40:
        if closest_target('Health Potion +1% health', list_obj) != None:
            print("h")
            return 'Health Potion +1% health'

listobjects = requests.get(connect + "/world/objects")

gooddata = listobjects.text
list_obj = json.loads(gooddata)


"""
def orbit_target(x, y):
"""


"""
for i in range(50):
    listobjects = requests.get("http://localhost:6001/api/world/objects")

    gooddata = listobjectes your characters armor class. The Mage receives the most armor from this and the Fighter receives the least. s.text
    list_obj = json.loads(gooddata)

    move_to_target('Shotgun', list_obj)   
"""