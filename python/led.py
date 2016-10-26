# imports needed libraries
import RPi.GPIO as GPIO
import time

# sets how pins are named
GPIO.setmode(GPIO.BCM)

# hides warnings
GPIO.setwarnings(False)

# delay in seconds, referenced later
delay = 0.005

# setup pins (either GPIO.OUT for ouputs or GPIO.IN for inputs)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
	# sets pin 24 output to low (could use 0, False, or GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	# sets pin 4 output to high (could use 1, True, or GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	# pauses for specified time in seconds
	time.sleep(delay)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(17, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(23, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	time.sleep(delay)
