import machine
import utime
import math
import time  # Import time module for delays
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

irPin = 17
myIR = machine.Pin(irPin, machine.Pin.IN)

redLED = machine.Pin(15, machine.Pin.OUT)

# Define pin numbers for ultrasonic sensor's TRIG and ECHO pins
TRIG = machine.Pin(17, machine.Pin.OUT)  # TRIG pin set as output
ECHO = machine.Pin(16, machine.Pin.IN)  # ECHO pin set as input


def distance():
    # Function to calculate distance in centimeters
    TRIG.low()  # Set TRIG low
    time.sleep_us(2)  # Wait for 2 microseconds
    TRIG.high()  # Set TRIG high
    time.sleep_us(10)  # Wait for 10 microseconds
    TRIG.low()  # Set TRIG low again

    # Wait for ECHO pin to go high
    while not ECHO.value():
        pass

    time1 = time.ticks_us()  # Record time when ECHO goes high

    # Wait for ECHO pin to go low
    while ECHO.value():
        pass

    time2 = time.ticks_us()  # Record time when ECHO goes low

    # Calculate the duration of the ECHO pin being high
    during = time.ticks_diff(time2, time1)

    # Return the calculated distance (using speed of sound)
    return during * 340 / 2 / 10000  # Distance in centimeters


servo = machine.PWM(machine.Pin(15))
servo.freq(50)

dist_90 = 18.6

count = [0,0,0,0,0,0,0,0,0,0]

x_joystick = machine.ADC(27)
y_joystick = machine.ADC(26)
z_switch = machine.Pin(22,machine.Pin.IN)

while True:
    x_value = x_joystick.read_u16()
    y_value = y_joystick.read_u16()
    servo_pos = round((x_value / 65536) * 6553 + 1638)
    angle = ((servo_pos - 1638) / (8191 - 1638)) * 180
    
    servo.duty_u16(servo_pos)
    z_value = z_switch.value()
    dis = distance()
    #print(dis)
    
    diff = math.cos(angle) + (dist_90 / dis)
    
    #print(diff)
    
    if -0.8 < diff and 0.8 > diff:
        count.append(0)
        print("0")
    else:
        if dis >= dist_90:
            count.append(1)
            print("1")
        else:
            count.append(2)
            print("2")
        
    count0 = 0
    count1 = 0
    count2 = 0
        
    for i in range(0, 10):
        if count[-i] == 0:
            count0 += 1
        elif count[-i] == 1:
            count1 += 1
        else:
            count2 += 1
        
    if count0 > count1 and count0 > count2:
        print("GROUND")
    elif count1 > count2:
        print("VOID")
    else:
        print("OBSTACLE")
        
    #print(angle)
    #print(x_value,y_value,z_value)
    utime.sleep_ms(30) 