# Copyright MMXXI Lam Ha haln@miamioh.edu
# Import libraries
import RPi.GPIO as GPIO
import time
from datetime import datetime

# Get the time of day and the number of chimes
datetime_1 = datetime.now()
hour = datetime_1.hour
minute = datetime_1.minute
c_h = hour%12 # number of chime 1
c_q = int(minute/15) # number of chime 2
c_m = minute%15 # number of chime 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Set pins 11 & 12 as outputs, and define as PWM chime0 and chime1
GPIO.setup(11,GPIO.OUT)
chime0 = GPIO.PWM(11,50) # pin 11 for chime0
GPIO.setup(12,GPIO.OUT)
chime1 = GPIO.PWM(12,50) # pin 12 for chime1

# Start PWM running
chime0.start(0)
chime1.start(0)

def chimer(chime):
    # Turn chime to 90 then back to 0 degrees
    chime.ChangeDutyCycle(7)
    time.sleep(0.5)
    chime.ChangeDutyCycle(0)
    time.sleep(1)
    chime.ChangeDutyCycle(2)
    time.sleep(0.5)
    chime.ChangeDutyCycle(0)
    print(chime, "ringed")

time.sleep(2)
# chime the hour
for x in range(1, c_h+1):
    chimer(chime0)
    time.sleep(0.75)
time.sleep(2)
# chime the quarters
for x in range(1, c_q+1):
    chimer(chime1)
    time.sleep(0.5)
    chimer(chime0)
    time.sleep(0.75)
time.sleep(2)
# chime the minutes
for x in range(1, c_m+1):
    chimer(chime1)
    time.sleep(0.75)
time.sleep(2)

#Clean things up at the end
chime0.stop()
chime1.stop()
GPIO.cleanup()
    
