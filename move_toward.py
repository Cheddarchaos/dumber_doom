
import requests
import aim_at_point
import math
connect = "http://localhost:6001/api/player"

r = requests.get(connect)

pos = r.json()["position"]

print(str(pos))

#moves a small distance towards a target x, y
def move_toward(x, y):
    r = requests.get(connect)

    dx = x - r.json()["position"]["x"]
    dy = y - r.json()["position"]["y"]

    pl_angle = r.json()["angle"]
    print("pl_angle: " + str(pl_angle))
    tar_angle = aim_at_point.find_angle(x, y)
    if tar_angle < 0:
        tar_angle += 360
    print("tar_angle: " + str(tar_angle))

    d_angle = tar_angle - pl_angle
    if d_angle < 0:
        d_angle += 360
    print("d_angle: " + str(d_angle))

    d_angle = (d_angle*math.pi)/180
    print("d_angle: " + str(d_angle))
    dist = 10

    print("dist: "+str(dist))
    d_forward = math.cos(d_angle)*dist
    print(d_forward)
    d_left = math.sin(d_angle)*dist
    print(d_left)

    if d_forward > 0:
        requests.post(connect + "/actions", json={'type': 'forward', 'amount': d_forward})
    else:
        requests.post(connect + "/actions", json={'type': 'backward', 'amount': abs(d_forward)})

    if d_left > 0:
        requests.post(connect + "/actions", json={'type': 'strafe-left', 'amount': d_left})
    else:
        requests.post(connect + "/actions", json={'type': 'strafe-right', 'amount': abs(d_left)})

"""""
Example:
x = r.json()["position"]["x"] + 500
y = r.json()["position"]["y"] + 200

while True:
    move_toward(x, y)
    if abs(x-r.json()["position"]["x"]) < 50 and abs(y-r.json()["position"]["y"]) < 50:
        break
r = requests.get(connect)

pos = r.json()["position"]

print(str(pos))