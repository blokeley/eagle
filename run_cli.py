"""Run motor using command line interface (CLI).

To run, open a terminal on the Raspberry Pi and type
$ sudo python3 run_cli.py

Copyright (C) 2015 Tom Oakley
MIT licence
"""

import logging

import motor


def get_command(prompt):
    """Split command into part and convert to floats."""
    command = input(prompt).split()

    # Return False if command is exit
    if not command or command[0] == 'exit':
        return False

    # Set motor drive time to 0.5 seconds if not given
    if len(command) == 1:
        command.append(0.5)

    # Convert arguments to integers
    return [float(num) for num in command[:2]]


if __name__ == '__main__':
    log_fmt = '%(asctime)s %(levelname)-8s %(message)s'
    date_fmt = '%H:%M:%S'
    logging.basicConfig(level=logging.DEBUG, format=log_fmt, datefmt=date_fmt)

    print('Motor driver.')
    print('Type: "duty time" e.g.:')
    print('"100 0.5" for 100% duty clockwise for 0.5 seconds,')
    print('"-100" for 100% duty counterclockwise forever,')
    print('"0" for stop and')
    print('"exit" to exit')

    prompt = 'motor> '
    command = get_command(prompt)

    try:
        with motor.Motor() as mtr:
            while command:
                logging.debug('Command = {}'.format(command))
                mtr.drive(*command)
                command = get_command(prompt)

    except KeyboardInterrupt:
        print('Exited by KeyboardInterrrupt')
