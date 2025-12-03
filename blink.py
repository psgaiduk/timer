
import time
from random import randint

from machine import I2C, PWM, Pin

from keypad import KeyPad
from led import LED, LEDColors
from I2C_LCD import I2CLcd
from irrecvdata import irGetCMD

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()
recvPin = irGetCMD(16)

try:
    if devices != []:
        lcd = I2CLcd(i2c, devices[0], 2, 16)
    else:
        print("No address found")
except:
    pass

kyePad = KeyPad(13, 12, 11, 10, 9, 8, 7, 6)

buzzer = PWM(Pin(27))  # GP15
led = LED(pins=[0, 1, 2])


def key():
    keyvalue = kyePad.scan()
    if keyvalue != None:
        print(keyvalue, end='\t')
        time.sleep_ms(300)
        return keyvalue
        
while True:
    input_key = key()
    irValue = recvPin.ir_read()
    if irValue:
        print(irValue, type(irValue))
    if input_key or irValue:
        print(input_key, 'input', type(input_key))
        if input_key == '1' or irValue == '0xff30cf':
            lcd.move_to(0, 0)
            lcd.putstr("Hello, world!")
            lcd.move_to(0, 1)
            lcd.putstr("Counter:")
        elif input_key == '2':
            for freq in [200, 400, 800, 1200, 1600, 2000]:
                buzzer.freq(freq)
                buzzer.duty_u16(30000)
                time.sleep(0.3)
            buzzer.deinit()
        elif input_key == '3':
            lcd.clear()
        elif input_key == '4':
            led.set_color(LEDColors.RED)
        elif input_key == '5':
            led.set_color(LEDColors.OFF)
            


