# imports the libraries needed for this program to run
from __future__ import division
import RPi.GPIO as GPIO
import picamera
import picamera.array
import colorsys
import numpy
import time
from time import sleep
import datetime

# opening message that indicates program is running
print("======= VIVA LA VIOLACEIN : AN AUTONOMOUS =======")
print("======= CONTROL SYSTEM FOR YEAST CULTURES =======")
print("\nThis Raspberry Pi setup coupled with a camera")
print("measures optical properties of cultures and")
print("directs the gradual release of inducer chemicals")
print("to maintain or change the culture's color over")
print("time.\n")

# assigns rgb values via array for four violacein colors
Color1 = [0, 0, 0] # no inputs
Color2 = [0, 0, 0] # copper input only
Color3 = [0, 0, 0] # galactose input only
color4 = [0, 0, 0] # both chemical inputs

GPIO.setmode(GPIO.BCM) # sets mode for pin names
GPIO.setwarnings(False) # prevents warning messages
GPIO.setup(17, GPIO.OUT) # sets pin 17 as output
GPIO.setup(18, GPIO.OUT) # sets pin 18 as output

# creates an instance of PiCamera and assigns it to variable camera
camera = picamera.PiCamera()

# takes user input for variable total
try:
    total = int(input("> Set total number of pictures to take: "))
except ValueError:
    print("\t\nERROR: Input must be an integer")

# takes user input for variable delay
try:
    delay = int(input("> Set delay between pictures in seconds: "))
except ValueError:
    print("\t\nERROR: Input must be an integer")

print()

GPIO.output(17, GPIO.LOW)

# takes pictures with delay and turns on LED when taking picture
count = 1
while (count <= total):
    sleep(delay)
    GPIO.output(18, GPIO.HIGH)
    camera.capture(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".jpg")
    print(str(count) + "     " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".jpg     " + "255 255 255")
    GPIO.output(18, GPIO.LOW)
    count += 1

GPIO.output(17, GPIO.HIGH)
