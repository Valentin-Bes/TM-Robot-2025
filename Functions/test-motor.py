import machine
import time
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

irPin = 17
myIR = machine.Pin(irPin, machine.Pin.IN)

motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)
    
def callback(IRBit, addr, ctrl):
    print(IRBit)
    
    if IRBit == 12:
        motor1A.high()
        time.sleep(0.8)
        motor1A.low()
    
    if IRBit == 24:
        motor2A.high()
        time.sleep(0.8)
        motor2A.low()
        
    if IRBit == -1:
        motor2A.high()
        time.sleep(0.2)
        motor2A.low()

IR = NEC_8(myIR, callback)