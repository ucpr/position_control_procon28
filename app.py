#!/usr/bin/env/python3

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while True:
        _, frame = cap.read()
        #HSV色空間に変換
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        #色検出
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("frame", frame)
#        cv2.imshow("mask", mask)
        cv2.imshow("res", res)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
 

if __name__ == "__main__":
    main()
