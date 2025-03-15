import time
from machine import Pin
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

irPin = 17
myIR = Pin(irPin, Pin.IN)

redLED = Pin(15, Pin.OUT)

def callback(IRBit, addr, ctrl):
    print(IRBit)
    
    if IRBit == 69:
        redLED.toggle()

IR = NEC_8(myIR, callback)

try:
    while True:
        pass
except KeyboardInterrupt:
    IR.close()
    print("Program Terminated")