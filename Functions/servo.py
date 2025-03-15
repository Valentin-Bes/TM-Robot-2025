import machine
import time
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

irPin = 17
myIR = machine.Pin(irPin, machine.Pin.IN)

servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def callback(IRBit, addr, ctrl):
    print(IRBit)
    
    if IRBit == 12:
        servo.duty_u16(1638)
    
    if IRBit == 24:
        servo.duty_u16(8191)
    
IR = NEC_8(myIR, callback)

 #max 8449-8450