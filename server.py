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
        "y": None,
    }},
    {"hcrs": {
        "x": None,
        "y": None,
    }},
]


def cv_res(p):
    x, y = cv_position.position(cap)
    p["cv"]["x"] = x
    p["cv"]["y"] = y
    return p

def hcrs_res(p):
    x, y = cv_position.position(cap)
    p["hcrs"]["x"] = x
    p["hcrs"]["y"] = y
    return p

@app.route("/json", methods=["GET"])
def get_position():
    p = copy.deepcopy(position)
    p[0] = cv_res(p[0])
    p[1] = hcrs_res(p[1])
    return jsonify(p)

if __name__ == "__main__":
    app.run()
