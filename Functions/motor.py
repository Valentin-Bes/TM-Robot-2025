import machine
import utime
import time

motor1A = machine.Pin(10, machine.Pin.OUT)
motor2A = machine.Pin(11, machine.Pin.OUT)

def clockwise():
    motor1A.high()
    motor2A.low()

def anticlockwise():
    motor1A.low()
    motor2A.high()

def stopMotor():
    motor1A.low()
    motor2A.low()

motor1A.high()
time.sleep(0.5)
motor1A.low()