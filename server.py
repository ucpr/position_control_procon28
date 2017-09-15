import copy
import cv2
from flask import Flask
from flask.json import jsonify

import cv_position
import hcrs_position

cap = cv2.VideoCapture(0)
app = Flask(__name__)
position = [
    {"cv": {
        "x": None,
        "z": None,
    }},
    {"hcrs": {
        "distance": None,
    }},
]


def cv_res(p):
    x, z = cv_position.position(cap)
    p["cv"]["x"] = x
    p["cv"]["z"] = z
    return p

def hcrs_res(p):
    dis = hcrs_position.position()
    p["hcrs"]["distance"] = dis
    return p

@app.route("/json", methods=["GET"])
def get_position():
    p = copy.deepcopy(position)
    p[0] = cv_res(p[0])
    p[1] = hcrs_res(p[1])
    return jsonify(p)

if __name__ == "__main__":
    app.run(port=5000)
