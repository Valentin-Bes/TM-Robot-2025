from machine import Pin,PWM
import time
import random 

redPin = 13
greenPin = 14
bluePin = 15

redLED=PWM(Pin(redPin))
greenLED=PWM(Pin(greenPin))
blueLED=PWM(Pin(bluePin))

redLED.freq(1000)
redLED.duty_u16(0)

greenLED.freq(1000)
greenLED.duty_u16(0)

blueLED.freq(1000)
blueLED.duty_u16(0)

while True:
    redBright = random.randint(0, 65550)
    greenBright = random.randint(0, 65550)
    blueBright = random.randint(0, 65550)
    
    redLED.duty_u16(redBright)
    greenLED.duty_u16(greenBright)
    blueLED.duty_u16(blueBright)
    time.sleep(.1)