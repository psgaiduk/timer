
import time

from machine import I2C, Pin

from buzzer import Buzzer, Ringtones
from keypad import KeyPad
from led import LED, LEDColors
from lcd import LCD
from remote_controller import irGetCMD


i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()
recvPin = irGetCMD(16)
lcd = LCD(i2c, devices[0], 2, 16)
keypad = KeyPad(13, 12, 11, 10, 9, 8, 7, 6)
buzzer = Buzzer(pin_number=27)
led = LED(pins=[0, 1, 2])


def key():
    keyvalue = keypad.scan()
    if keyvalue is not None:
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
            lcd.putstr("Hello, world!!!")
            lcd.move_to(0, 1)
            lcd.putstr("Counter:")
        elif input_key == '2':
            buzzer.buzz_by_ringtone(Ringtones.WORK_DONE)
        elif input_key == '3':
            buzzer.buzz_by_ringtone(Ringtones.BREAK_DONE)
            lcd.clear()
        elif input_key == '4':
            buzzer.buzz_by_ringtone(Ringtones.STOP_REMINDER)
            led.set_color(LEDColors.RED)
        elif input_key == '5':
            led.set_color(LEDColors.OFF)
