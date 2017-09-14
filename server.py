import copy
import cv2
from flask import Flask
from flask.json import jsonify

import cv_position
#import hcrs_position

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


def cv_p():
    x, y = cv_position.position(cap)
    print(x, y)
    return x, y

def hcrs_p():
    x, y = hcrs_position.position()
    print(x, y)
    return x, y

@app.route("/json", methods=["GET"])
def get_position():
    p = copy.deepcopy(position)
    cv_p()
    return jsonify({"position": position})

if __name__ == "__main__":
    app.run(debug=True)
