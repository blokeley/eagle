"""Run motor using command line interface (CLI).

To run, open a terminal on the Raspberry Pi and type
$ sudo python3 run_cli.py

Copyright (C) 2015 Tom Oakley
MIT licence
"""

import logging

import RPi.GPIO as gpio

import motor


if __name__ == '__main__':
    log_fmt = '%(asctime)s %(levelname)-8s %(message)s'
    date_fmt = '%H:%M:%S'
    logging.basicConfig(level=logging.DEBUG, format=log_fmt, datefmt=date_fmt)

    mtr = motor.Motor()

    print('Motor driver. Type:')
    print('"100" for clockwise,')
    print('"-100" for counterclockwise,')
    print('"0" for stop and')
    print('"exit" to exit')

    prompt = 'motor> '
    command = input(prompt)

    try:
        while command != 'exit':
            mtr.drive(int(command))
            command = input(prompt)

    finally:
        gpio.cleanup()
