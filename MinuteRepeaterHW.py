# Copyright MMXXI Lam Ha haln@miamioh.edu
# Import libraries
import RPi.GPIO as GPIO
import time
from datetime import datetime
from GetTime import Time
# Get the time of day and the number of chimes

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Set pins 11 & 12 as outputs, and define as PWM chime0 and chime1
GPIO.setup(11,GPIO.OUT)
chime0 = GPIO.PWM(11,50) # pin 11 for chime0
GPIO.setup(12,GPIO.OUT)
chime1 = GPIO.PWM(12,50) # pin 12 for chime1

def chimer(chime):
    # Turn chime to 90 then back to 0 degrees
    chime.ChangeDutyCycle(7)
    time.sleep(0.5)
    chime.ChangeDutyCycle(0)
    time.sleep(1)
    chime.ChangeDutyCycle(2)
    time.sleep(0.5)
    chime.ChangeDutyCycle(0)
def chime(hour, minute):
    c_h = hour%12 # number of chime 1
    c_q = int(minute/15) # number of chime 2
    c_m = minute%15 # number of chime 3
    chime0.start(0) # Start PWM running
    chime1.start(0)
    time.sleep(1)
    for x in range(1, c_h+1): # chime the hour
        chimer(chime0)
        time.sleep(0.75)
        time.sleep(2)
    for x in range(1, c_q+1): # chime the quarters
        chimer(chime1)
        time.sleep(0.5)
        chimer(chime0)
        time.sleep(0.75)
        time.sleep(2)
    for x in range(1, c_m+1): # chime the minutes
        chimer(chime1)
        time.sleep(0.75)
    time.sleep(2) #Clean things up at the end
    chime0.stop()
    chime1.stop()
    GPIO.cleanup()

code = ''
while True:
    print("Enter Airport Code or City Name, 'current time', or 'quit' to exit")
    code = input()
    if code == 'quit':
        break
    if code == 'current time':
        hour = datetime.now().hour
        minute = datetime.now().minute
        chime(hour, minute)
        print("Done")
    else:
        t = Time(code)
        if t.time == None:
            print("Try again")
        else:
            hour = t.time.hour
            minute = t.time.minute
            chime(hour, minute)