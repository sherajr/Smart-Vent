#!/usr/bin/env python

#Import libraries I may need
import time
import atexit
import pigpio
import RPi.GPIO as GPIO
import sqlite3 as lite
import Adafruit_DHT

#Set sensor to the DHT22 sensor using Adafruit syntax
sensor = Adafruit_DHT.DHT22

#Set mode to BCM (rather than board) so pin numbers are the same as the GPIO#
GPIO.setmode(GPIO.BCM)

#Set GPIO pin(s) relay is connected to
pinList = [14]

#Set GPIO pin DHT22 sensor is connected to
pin = 4

#Set GPIO pin button is connected to
bt = 26

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT)

    GPIO.output(i, GPIO.LOW)

# set button as input
    GPIO.setup(bt, GPIO.IN)


try:
    while True:
        input_value = GPIO.input(bt)
        
        if input_value == False:

            GPIO.output(i, GPIO.HIGH)

        elif input_value == True:

            GPIO.output(i, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(i, GPIO.LOW)
    GPIO.cleanup(i)
    pass

         
