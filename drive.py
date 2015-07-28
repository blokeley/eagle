"""Motor drive utilities.

See Adafruit lesson 9 for circuit diagram.

To run, open a terminal on the Raspberry Pi and type
$ sudo python3 drive.py

Copyright (C) 2015 Tom Oakley
MIT licence
"""

import logging
import sys

import RPi.GPIO as gpio


def drive(direction):
    """Drive the motor:
    
     100 for clockwise
    -100 for counter clockwise
       0 for stop
    """

    assert direction in (-100, 100, 0)

    if direction > 0:
        gpio.output(in1_pin, True)
        gpio.output(in2_pin, False)
        gpio.output(pwm_pin, True)

    elif direction < 0:
        gpio.output(in1_pin, False)
        gpio.output(in2_pin, True)
        gpio.output(pwm_pin, True)

    else:
        # Stop the motor
        gpio.output(in1_pin, False)
        gpio.output(in2_pin, False)
        gpio.output(pwm_pin, False)


if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    in1_pin = 4
    in2_pin = 17
    pwm_pin = 18

    gpio.setup(in1_pin, gpio.OUT)
    gpio.setup(in2_pin, gpio.OUT)
    gpio.setup(pwm_pin, gpio.OUT)

    # Set up PWM
    # pwm = gpio.PWM(pwm_pin, 20000)
    # pwm.start(100)

    print('Motor driver. Type:')
    print('"100" for clockwise,')
    print('"-100" for counterclockwise,')
    print('"0" for stop and')
    print('"exit" to exit')

    prompt = 'motor> '
    command = input(prompt)

    try:
        while command != 'exit':
            drive(int(command))
            command = input(prompt)

    finally:
        gpio.cleanup()
