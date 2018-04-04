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



"""
Grab sensor reading using 'read_retry' which will
try 15 times (once every 2 seconds) to get a reading.

Using a try loop Make it grab a measurement every X (must be more than 2) seconds
until it is interupted by a keystroke which would end the program.

See Relay Loop for turning fan on or off based on sensor measurements
"""

HH= 80 #High Humidity value
HL= 70 #Low Humidity value
timewait= 3 #Time interval between measurements in seconds

try:
    while True:
        input_value = GPIO.input(bt)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        temperature = temperature * 9/5.0 + 32
        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity))
        if input_value == False or humidity >HH:

            GPIO.output(i, GPIO.HIGH)

            time.sleep(3)

        elif input_value == True and humidity <HL:

                GPIO.output(i, GPIO.LOW)

                if input_value == False:

                    GPIO.output(i, GPIO.HIGH)

                time.sleep(timewait)

except KeyboardInterrupt:
    GPIO.output(i, GPIO.LOW)
    GPIO.cleanup(i)
    pass


#Display results of reading
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading.')


"""
Put Temp and Humidity data into Database

Once I figure that out I'll do it!
"""
