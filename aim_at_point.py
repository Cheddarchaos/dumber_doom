
import requests
import random
import math

from pprint import pprint as pp


r = requests.get("http://localhost:6001/api/player")

angle1 = r.json()["angle"]
pos = r.json()["position"]

print(str(pos))

def turn_to_angle(angle):
    r = requests.get("http://localhost:6001/api/player")
    start_angle = r.json()["angle"]
    if angle == 0 or angle == 360:
        rand = random.uniform(0, 1)
        if rand == 1:
            angle = 1
        else:
            angle = 359

    if angle < 0:
        angle += 360

    delta_angle = angle - start_angle

    if delta_angle < 0:
        delta_angle += 360

    if delta_angle > 180:
        requests.post("http://localhost:6001/api/player/turn", json={"type": "right", "target_angle": angle})
    else:
        requests.post("http://localhost:6001/api/player/turn", json={"type": "left", "target_angle": angle})

def find_angle(x, y):
    r = requests.get("http://localhost:6001/api/player")
    dx = x - r.json()["position"]["x"]
    dy = y - r.json()["position"]["y"]
    angle_rad = math.atan2(dy,dx)
    angle = (angle_rad*(180/math.pi))
    return angle

def aim_point(x, y):
    angle = find_angle(x,y)
    turn_to_angle(angle)



aim_point(r.json()["position"]["x"],r.json()["position"]["y"]+10)