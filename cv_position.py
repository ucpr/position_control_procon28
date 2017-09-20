#!/usr/bin/env/python3

from collections import deque
import imutils
import cv2
import numpy as np

LOWER_BLUE = np.array([110, 50, 50])
UPPER_BLUE = np.array([130, 255, 255])
pts = deque(maxlen=64)


def diff(a, b):
    """
    a : tuple # (width, height)
    b : tuple # (width, height) 
    """
    width = a[0] - b[0]
    height = a[1] - b[1]

    return width, height
    
def ptoc(w, h, dpi=72):
    pixel = dpi / 2.54
    width = w / pixel 
    height = h / pixel

    return width, height

def position(cap):
    if cap.isOpened() is False:
        raise("IO Error")

    _, frame = cap.read()
    frame = imutils.resize(frame, width=640, height=480)
    height, width = frame.shape[:2]

    #HSV色空間に変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #色検出
    mask = cv2.inRange(hsv, LOWER_BLUE, UPPER_BLUE)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #輪郭の抽出
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    pts.appendleft(center)

    cv2.circle(frame, (width // 2, height // 2), 5, (255, 0, 0), 10)

    if center is not None:
        w, h = diff((width // 2, height // 2), center)
        w, h = ptoc(w, h)
    else:
        w, h = "None", "None"

    return w, h 

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    print(position(cap))
