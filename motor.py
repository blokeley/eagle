"""Motor drive utilities.

See Adafruit lesson 9 for circuit diagram.

Copyright (C) 2015 Tom Oakley
MIT licence
"""

import logging
import time

import RPi.GPIO as GPIO


class Motor():

    def __enter__(self):
        """Enter context manager to use with `with` statement."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self._in1_pin = 4
        self._in2_pin = 17
        self._pwm_pin = 18

        GPIO.setup(self._in1_pin, GPIO.OUT)
        GPIO.setup(self._in2_pin, GPIO.OUT)
        GPIO.setup(self._pwm_pin, GPIO.OUT)

        # Set up PWM
        # pwm = GPIO.PWM(_pwm_pin, 20000)
        # pwm.start(100)

        self._drive_count = 0

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Exit context manager to use with `with` statement."""
        GPIO.cleanup()

    def drive(self, duty, time_=0.5):
        """Drive the motor.

        duty is:
             100 for clockwise
            -100 for counter clockwise
               0 for stop

        time_ is the time in seconds. Set to negative for no timeout
        """

        assert -100 <= duty <= 100

        if duty == 0:
            # Stop the motor
            GPIO.output(self._in1_pin, False)
            GPIO.output(self._in2_pin, False)
            GPIO.output(self._pwm_pin, False)
            return

        self._drive_count += 1
        fmt = 'Drive #{} at {} duty for {} s'
        logging.debug(fmt.format(self._drive_count, duty. time_))

        if duty > 0:
            GPIO.output(self._in1_pin, True)
            GPIO.output(self._in2_pin, False)
            GPIO.output(self._pwm_pin, True)

        else:
            GPIO.output(self._in1_pin, False)
            GPIO.output(self._in2_pin, True)
            GPIO.output(self._pwm_pin, True)

        if time_ >= 0:
            # Sleep whilst the motor runs
            time.sleep(time_)
            # Stop the motor
            self.drive(0)
