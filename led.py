#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT)


def printTemperature():
    temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    print("LA TEMPERATURE DE GPU {}".format(temp[5:]))


def controlLED():
    try:
        while True:
            user_input = input(
                "CONTROL LED PAR '0' '1' (Ctrl-C POUR SORTIR): ")
            if user_input is "1":
                GPIO.output(18, GPIO.HIGH)
                print("LED is on")
            elif user_input is "0":
                GPIO.output(18, GPIO.LOW)
                print("LED is off")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")


setupGPIO()
printTemperature()

controlLED()
