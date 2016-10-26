
import RPi.GPIO as GPIO
import time

# sets how pins are named
GPIO.setmode(GPIO.BCM)

# hides warnings
GPIO.setwarnings(False)

# pins for stepper motor
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

while True:
                GPIO.output(enable_pin, 0)
                quit()
