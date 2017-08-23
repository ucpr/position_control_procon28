#!/usr/bin/env/python3

from collections import deque
import imutils
import cv2
import numpy as np

LOWER_BLUE = np.array([110, 50, 50])
UPPER_BLUE = np.array([130, 255, 255])
LOWER_RED = np.array([150, 70, 70])
UPPER_RED = np.array([255, 0, 0])
pts = deque(maxlen=64)

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while True:
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
        #print(center) 

        cv2.imshow("frame", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
