from machine import PWM, Pin


class LEDColors:
    RED = (65535, 0, 0)
    GREEN = (0, 65535, 0)
    BLUE = (0, 0, 65535)
    WHITE = (65535, 65535, 65535)
    OFF = (65535, 65535, 65535)


class LED:
    """A simple LED class to control an LED connected to a specified pin."""

    def __init__(self, pins: list) -> None:
        """Initialize the LED with the given pin numbers."""
        freq_num = 10000
        self.pwm0 = PWM(Pin(pins[0]))
        self.pwm1 = PWM(Pin(pins[1]))
        self.pwm2 = PWM(Pin(pins[2]))
        self.pwm0.freq(freq_num)
        self.pwm1.freq(freq_num)
        self.pwm2.freq(freq_num)

    def set_color(self, color: tuple) -> None:
        """Set the LED color."""
        self.pwm0.duty_u16(color[0])
        self.pwm1.duty_u16(color[1])
        self.pwm2.duty_u16(color[2])
