from machine import Pin
import time

redLED = Pin(15, Pin.OUT)

while True:
    redLED.toggle()
    time.sleep(.5)