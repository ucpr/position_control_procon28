#!/usr/bin/env python3
 
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
 
GPIO.setmode(GPIO.BOARD)
TRIG1 = 11
ECHO1 = 13
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)


def position():
    """
    超音波を使ってドローン間がどのくらい開いているかを返す

    Return
    ------
    distance: float
    """
    GPIO.output(TRIG1, GPIO.LOW)
    time.sleep(0.3)
       
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)

    signal_off = 0
    signal_on  = 0
 
    while GPIO.input(ECHO1) == 0:
        signal_off = time.time()
         
    while GPIO.input(ECHO1) == 1:
        signal_on = time.time()

    timepassed = signal_on - signal_off
    distance = timepassed * 17000
#    GPIO.cleanup()
    return distance


if __name__ == "__main__":
    while True:
        print(position())
