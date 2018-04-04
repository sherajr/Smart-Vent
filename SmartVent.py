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

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT)

    GPIO.output(i, GPIO.HIGH)

"""
Grab sensor reading using 'read_retry' which will
try 15 times (once every 2 seconds) to get a reading.

Using a try loop Make it grab a measurement every X (must be more than 2) seconds
until it is interupted by a keystroke which would end the program.

See Relay Loop for turning fan on or off based on sensor measurements
"""

HH= 55 #High Humidity value
HL= 45 #Low Humidity value
timewait= 3 #Time interval between measurements in seconds

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        #Convert from Celcius to Fahrenheit comment out if Celcius is desired
        temperature = temperature * 9/5.0 + 32
        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity))
        #Relay loop
        if humidity >HH:

            GPIO.output(i, GPIO.LOW)

        elif humidity <HL:

            GPIO.output(i, GPIO.HIGH)
        time.sleep(timewait)
except KeyboardInterrupt:
    GPIO.output(i, GPIO.HIGH)
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




