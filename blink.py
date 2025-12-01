
import time

from machine import I2C, PWM, Pin

from keypad import KeyPad
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

from machine import Pin, PWM
from random import randint
import time

pins = [2, 3, 4]
freq_num = 10000

pwm0 = PWM(Pin(pins[0]))  #set PWM
pwm1 = PWM(Pin(pins[1]))
pwm2 = PWM(Pin(pins[2]))
pwm0.freq(freq_num)
pwm1.freq(freq_num)
pwm2.freq(freq_num)

def setColor(r, g, b):
    pwm0.duty_u16(65535 - r)
    pwm1.duty_u16(65535 - g)
    pwm2.duty_u16(65535 - b)

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
            try:
                red   = randint(0, 65535)
                green = randint(0, 65535)
                blue  = randint(0, 65535)
                setColor(red, green, blue)
                time.sleep_ms(200)
            except:
                pwm0.deinit()
                pwm1.deinit()
                pwm2.deinit()


