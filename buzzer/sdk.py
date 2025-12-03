from time import sleep

from machine import PWM, Pin


class Ringtones:
    """Predefined ringtones for the Buzzer class."""

    WORK_DONE = [(800, 0.3), (1000, 0.3), (1200, 0.3), (1500, 0.5), (1200, 0.3), (1000, 0.3)]
    BREAK_DONE = [(1000, 0.2), (1200, 0.2), (1400, 0.2), (1200, 0.2), (1000, 0.2)]
    STOP_REMINDER = [(1500, 0.1), (1200, 0.1), (1500, 0.1)]


class Buzzer:
    """A simple Buzzer class to control a buzzer connected to a specified pin."""

    def __init__(self, pin_number: int) -> None:
        """Initialize the Buzzer with the given pin number."""
        self.buzzer = PWM(Pin(pin_number))

    def buzz_by_ringtone(self, ringtone: list) -> None:
        """
        Play a ringtone represented as a list of frequencies.

        :param ringtone: List of frequencies to play.
        """
        for freq, duration in ringtone:
            self.buzzer.freq(freq)
            self.buzzer.duty_u16(30000)
            sleep(duration)
        self.buzzer.deinit()
