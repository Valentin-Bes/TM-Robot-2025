import machine
import utime

x_joystick = machine.ADC(27)
y_joystick = machine.ADC(26)
z_switch = machine.Pin(22,machine.Pin.IN)

red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))
red.freq(1000)
green.freq(1000)
blue.freq(1000)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def color_to_duty(rgb_value):
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value

def color_set(red_value,green_value,blue_value):
    red.duty_u16(color_to_duty(red_value))
    green.duty_u16(color_to_duty(green_value))
    blue.duty_u16(color_to_duty(blue_value))

while True:
    x_value = x_joystick.read_u16()
    y_value = y_joystick.read_u16()
    z_value = z_switch.value()
    print(x_value,y_value,z_value)
    
    r = (x_value / 65535) * 255
    g = (y_value / 65535) * 255
    if z_value == 0:
        b = 255
    else:
        b = 0
    
    color_set(r, g, b)
    utime.sleep_ms(50) 