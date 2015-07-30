"""Motor drive utilities.

See Adafruit lesson 9 for circuit diagram.

Copyright (C) 2015 Tom Oakley
MIT licence
"""

import logging
import time

import RPi.GPIO as gpio


class Motor():

    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        self.in1_pin = 4
        self.in2_pin = 17
        self.pwm_pin = 18

        gpio.setup(self.in1_pin, gpio.OUT)
        gpio.setup(self.in2_pin, gpio.OUT)
        gpio.setup(self.pwm_pin, gpio.OUT)

        # Set up PWM
        # pwm = gpio.PWM(pwm_pin, 20000)
        # pwm.start(100)

    def drive(self, duty, time_=0.5):
        """Drive the motor.

        duty is:
             100 for clockwise
            -100 for counter clockwise
               0 for stop

        time_ is the time in seconds. Set to negative for no timeout
        """

        assert duty in (-100, 100, 0)

        if duty == 0:
            # Stop the motor
            gpio.output(self.in1_pin, False)
            gpio.output(self.in2_pin, False)
            gpio.output(self.pwm_pin, False)
            return

        logging.debug('Driving motor at {} for {}'.format(duty. time_))

        if duty > 0:
            gpio.output(self.in1_pin, True)
            gpio.output(self.in2_pin, False)
            gpio.output(self.pwm_pin, True)

        else:
            gpio.output(self.in1_pin, False)
            gpio.output(self.in2_pin, True)
            gpio.output(self.pwm_pin, True)

        if time_ >= 0:
            # Sleep whilst the motor runs
            time.sleep(time_)
            # Stop the motor
            self.drive(0)
