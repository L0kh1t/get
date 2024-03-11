import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
for i in range(300):
    GPIO.output(25, 1)
    time.sleep(1)
    GPIO.output(25, 0)
    time.sleep(1)
       