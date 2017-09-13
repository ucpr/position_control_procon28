#!/usr/bin/env python3
 
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
 
GPIO.setmode(GPIO.BOARD)
TRIG1 = 11
ECHO1 = 13
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

def position():
    GPIO.output(TRIG1, GPIO.LOW)
    time.sleep(0.3)
       
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)

    signaloff = 0
    signalon  = 0
 
    while  GPIO.input(ECHO1) == 0:
        signaloff = time.time()
         
    while GPIO.input(ECHO1) == 1:
        signalon = time.time()

    timepassed = signalon - signaloff
    distance = timepassed * 17000
    GPIO.cleanup()
    return distance

if __name__ == "__main__":
    while True:
        print(reading())
